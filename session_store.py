from collections import defaultdict
import time

sessions = defaultdict(dict)

def init_session(sessionId):
    if sessionId not in sessions:
        sessions[sessionId] = {
            "messages": [],
            "intelligence": {
                "bankAccounts": [],
                "upiIds": [],
                "phishingLinks": [],
                "phoneNumbers": [],
                "suspiciousKeywords": []
            },
            "scamDetected": False,
            "startTime": time.time(),
            "callbackSent": False
        }
    return sessions[sessionId]
