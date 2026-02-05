SCAM_KEYWORDS = [
    "urgent",
    "verify",
    "blocked",
    "suspended",
    "upi",
    "otp",
    "bank",
    "click",
    "link"
]

def is_scam(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in SCAM_KEYWORDS)
