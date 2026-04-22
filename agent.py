from intent import detect_intent
from rag import get_answer
from tools import mock_lead_capture

user_state = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None,
    "collecting": False
}

def handle_chat(message):
    global user_state

    # If already collecting lead info
    if user_state["collecting"]:
        if not user_state["name"]:
            user_state["name"] = message
            return "Nice to meet you! What's your email?"

        elif not user_state["email"]:
            user_state["email"] = message
            return "Which platform do you create on? (YouTube/Instagram)"

        elif not user_state["platform"]:
            user_state["platform"] = message
            
            # Call tool only AFTER collecting all
            mock_lead_capture(
                user_state["name"],
                user_state["email"],
                user_state["platform"]
            )

            user_state["collecting"] = False
            return "You're all set! 🚀 We'll reach out soon."

    intent = detect_intent(message)

    if intent == "greeting":
        return "Hey! 👋 How can I help you today?"

    elif intent == "info":
        return get_answer(message)

    elif intent == "high_intent":
        user_state["collecting"] = True
        return "Awesome! Let's get you started. What's your name?"

    return "Hmm, I didn't get that. Ask me about pricing or plans!"
