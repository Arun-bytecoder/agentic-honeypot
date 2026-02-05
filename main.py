from fastapi import FastAPI, Depends, BackgroundTasks
from pydantic import BaseModel
from typing import List, Dict, Optional

from auth import verify_api_key
from detector import is_scam
from agent import generate_agent_reply
from extractor import extract_intelligence
from callback import send_guvi_callback

app = FastAPI(title="Agentic Honeypot API")

# =========================
# IN-MEMORY SESSION STORE
# =========================
sessions: Dict[str, Dict] = {}

# =========================
# REQUEST MODELS
# =========================
class Message(BaseModel):
    sender: str
    text: str
    timestamp: int

class HoneypotRequest(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: List[dict] = []
    metadata: Optional[dict] = None

# =========================
# CONSTANTS
# =========================
MIN_MESSAGES_FOR_CALLBACK = 5

# =========================
# MAIN ENDPOINT
# =========================
@app.post("/honeypot")
def honeypot(
    data: HoneypotRequest,
    background_tasks: BackgroundTasks,
    _=Depends(verify_api_key)
):
    # -------------------------
    # Initialize session
    # -------------------------
    if data.sessionId not in sessions:
        sessions[data.sessionId] = {
            "totalMessages": 0,
            "scamDetected": False,
            "callbackSent": False,
            "intelligence": {
                "bankAccounts": [],
                "upiIds": [],
                "phishingLinks": [],
                "phoneNumbers": [],
                "suspiciousKeywords": []
            }
        }

    session = sessions[data.sessionId]

    # -------------------------
    # Engagement depth (SINGLE SOURCE OF TRUTH)
    # -------------------------
    session["totalMessages"] += 1

    # -------------------------
    # Scam detection
    # -------------------------
    if data.message.sender.lower() == "scammer" or is_scam(data.message.text):
        session["scamDetected"] = True

    # -------------------------
    # Intelligence extraction
    # -------------------------
    intel = extract_intelligence(data.message.text)
    for key in session["intelligence"]:
        for value in intel.get(key, []):
            if value not in session["intelligence"][key]:
                session["intelligence"][key].append(value)

    # -------------------------
    # Agent reply
    # -------------------------
    reply = generate_agent_reply(data.conversationHistory)

    # -------------------------
    # GUVI callback (NON-BLOCKING, SAFE)
    # -------------------------
    if (
        session["scamDetected"]
        and session["totalMessages"] >= MIN_MESSAGES_FOR_CALLBACK
        and not session["callbackSent"]
    ):
        background_tasks.add_task(
            send_guvi_callback,
            data.sessionId,
            session["scamDetected"],
            session["totalMessages"],   # ✅ CORRECT
            session["intelligence"]
        )
        session["callbackSent"] = True

    # -------------------------
    # Immediate response
    # -------------------------
    return {
        "status": "success",
        "reply": reply
    }
