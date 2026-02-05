import os
import json
import requests

GUVI_CALLBACK_URL = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"

# Read debug flag from environment
DEBUG_CALLBACK = os.getenv("DEBUG_CALLBACK", "false").lower() == "true"

def send_guvi_callback(
    session_id: str,
    scam_detected: bool,
    total_messages: int,
    intelligence: dict
):
    payload = {
        "sessionId": session_id,
        "scamDetected": scam_detected,
        "totalMessagesExchanged": total_messages,
        "extractedIntelligence": {
            "bankAccounts": intelligence.get("bankAccounts", []),
            "upiIds": intelligence.get("upiIds", []),
            "phishingLinks": intelligence.get("phishingLinks", []),
            "phoneNumbers": intelligence.get("phoneNumbers", []),
            "suspiciousKeywords": intelligence.get("suspiciousKeywords", [])
        },
        "agentNotes": "Repeated urgency, impersonation of bank staff, credential harvesting"
    }

    # 🔍 LOCAL DEBUG ONLY
    if DEBUG_CALLBACK:
        print("\n====== GUVI CALLBACK PAYLOAD (LOCAL DEBUG) ======")
        print(json.dumps(payload, indent=2))
        print("================================================\n")

    try:
        response = requests.post(
            GUVI_CALLBACK_URL,
            json=payload,
            timeout=5
        )

        if DEBUG_CALLBACK:
            print(f"GUVI CALLBACK RESPONSE: {response.status_code}")

    except Exception as e:
        if DEBUG_CALLBACK:
            print("⚠ CALLBACK FAILED:", e)
        # Silent fail in production
        pass
