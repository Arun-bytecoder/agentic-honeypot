import requests

GUVI_CALLBACK_URL = "https://hackathon.guvi.in/api/updateHoneyPotFinalResult"

def send_guvi_callback(
    session_id: str,
    scam_detected: bool,
    messages: list,
    intelligence: dict
):
    payload = {
        "sessionId": session_id,
        "scamDetected": scam_detected,
        "totalMessagesExchanged": len(messages),
        "extractedIntelligence": {
            "bankAccounts": intelligence.get("bankAccounts", []),
            "upiIds": intelligence.get("upiIds", []),
            "phishingLinks": intelligence.get("phishingLinks", []),
            "phoneNumbers": intelligence.get("phoneNumbers", []),
            "suspiciousKeywords": intelligence.get("suspiciousKeywords", [])
        },
        "agentNotes": "Scammer used urgency and verification tactics"
    }

    try:
        requests.post(
            GUVI_CALLBACK_URL,
            json=payload,
            timeout=5
        )
    except Exception:
        # Silent fail (VERY IMPORTANT — never break main API)
        pass
    
    print("✅ GUVI CALLBACK SENT for session:", session_id)


