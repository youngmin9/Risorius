import streamlit as st
import random

# Define empathetic responses
empathetic_responses = [
    "I'm really sorry to hear that.",
    "I can understand how you're feeling. Please know that I'm here to chat.",
    "I'm here to listen. Please take your time.",
    "It sounds like you're going through a tough time. I'm here to support you.",
    "I'm sending you virtual support and positive thoughts.",
    # ... Add more responses here ...
    "Remember that you're not alone in this. Reach out to your loved ones for support.",
    "Take a deep breath and give yourself permission to feel how you feel.",
    "I wish I could give you a real hug right now. Sending you a virtual one 🤗",
    "You're stronger than you know. You've got this!",
    "Sometimes it's okay not to be okay. Allow yourself to heal at your own pace."
    # ... Add more responses here ...
]

def get_empathetic_response(user_message):
    # In a real implementation, you might use sentiment analysis here
    # to tailor the response based on the emotional tone of the user's message.
    # For simplicity, we'll just pick a response randomly.
    return random.choice(empathetic_responses)

# Streamlit app
def main():
    st.title("Sympathy Chatbot")
    user_message = st.text_input("Enter your message:")
    
    if user_message:
        bot_response = get_empathetic_response(user_message)
        st.text("You: " + user_message)
        st.text("Bot: " + bot_response)

if __name__ == "__main__":
    main()
