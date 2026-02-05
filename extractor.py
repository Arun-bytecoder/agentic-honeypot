import re

SUSPICIOUS_KEYWORDS = [
    "otp", "urgent", "blocked", "verify", "suspended",
    "account", "freeze", "limited time", "immediately",
    "upi", "debit card", "cvv", "pin"
]

def extract_intelligence(text: str) -> dict:
    intelligence = {
        "bankAccounts": [],
        "upiIds": [],
        "phishingLinks": [],
        "phoneNumbers": [],
        "suspiciousKeywords": []
    }

    # Phone numbers
    intelligence["phoneNumbers"] = re.findall(r"\+?\d[\d\- ]{8,}\d", text)

    # UPI IDs
    intelligence["upiIds"] = re.findall(r"[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}", text)

    # Phishing links
    intelligence["phishingLinks"] = re.findall(r"https?://\S+", text)

    # Bank account numbers (10–18 digits)
    intelligence["bankAccounts"] = re.findall(r"\b\d{10,18}\b", text)

    # Suspicious keywords
    lowered = text.lower()
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in lowered:
            intelligence["suspiciousKeywords"].append(keyword)

    return intelligence
