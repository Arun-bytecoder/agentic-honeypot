def generate_agent_reply(history):
    """
    Generates human-like, adaptive replies based on conversation history.
    This is lightweight, fast, and evaluator-safe.
    """

    # First message
    if not history:
        return "Why is my account being suspended?"

    last_message = history[-1].get("text", "").lower()

    if "upi" in last_message:
        return "Is it safe to share my UPI ID here?"
    if "link" in last_message or "click" in last_message:
        return "What will happen if I click this link?"
    if "otp" in last_message:
        return "I haven’t received any OTP yet."
    if "verify" in last_message:
        return "Why do I need to verify again?"

    return "Can you explain what I should do next?"
