import gradio as gr
from agent import handle_chat

def chat_interface(message, history):
    return handle_chat(message)

demo = gr.ChatInterface(
    fn=chat_interface, 
    title="AutoStream AI Agent",
    description="A conversational AI agent that simulates a SaaS sales assistant for AutoStream."
)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
