from agent import handle_chat

print("AutoStream AI Agent (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        break

    response = handle_chat(user_input)
    print("Agent:", response)
