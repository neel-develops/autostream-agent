import json

def get_answer(query):
    with open("data.json") as f:
        data = json.load(f)

    query = query.lower()

    if "price" in query or "plan" in query:
        return f"""
📦 AutoStream Plans:

Basic Plan:
{data['pricing']['basic']['price']}
Features: {', '.join(data['pricing']['basic']['features'])}

Pro Plan:
{data['pricing']['pro']['price']}
Features: {', '.join(data['pricing']['pro']['features'])}
"""

    elif "refund" in query or "policy" in query:
        return "\n".join(data["policies"])

    elif "feature" in query:
        return "✨ AutoStream Core Features:\n- " + "\n- ".join(data.get("core_features", [])) + "\n\nAnd much more! Let me know if you want to check out our pricing plans."

    return "Ask me about pricing, plans, or features!"
