import google.generativeai as genai
import gradio as gr

# 🔹 Configure API key
genai.configure(api_key="AIzaSyAc8H9L10-2AvHO2q_9AqdfpaeTXJ7kla0")  # Replace with your Gemini API key

# 🔹 Create model object
model = genai.GenerativeModel("gemini-pro")

# 🔹 Chat function
def chat_with_gemini(message, history):
    # Convert Gradio chat history into Gemini format
    history_text = ""
    for human, bot in history:
        history_text += f"User: {human}\nBot: {bot}\n"

    prompt = history_text + f"User: {message}\nBot:"

    response = model.generate_content(prompt)
    reply = response.text

    history.append((message, reply))
    return reply, history

# 🔹 Create UI
demo = gr.ChatInterface(
    fn=chat_with_gemini,
    title="Mini-Chatbot (Gemini API)",
    description="Ask me anything! Powered by Google Gemini Pro."
)

demo.launch()
