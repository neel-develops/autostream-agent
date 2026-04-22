def detect_intent(message):
    message = message.lower()

    if any(word in message for word in ["hi", "hello", "hey"]):
        return "greeting"
    
    elif any(word in message for word in ["price", "pricing", "cost", "plan"]):
        return "info"
    
    elif any(word in message for word in ["buy", "subscribe", "try", "sign up", "start", "want"]):
        return "high_intent"
    
    return "unknown"
