import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

def get_angry_level(sentiment):
    if sentiment < -0.5:
        return "Very Angry 😡😠🤬"
    elif sentiment < 0:
        return "Somewhat Angry 😣😒"
    else:
        return "Not Angry 🙂😊"

def main():
    st.title("Angry Level Chatbot")
    st.write("Enter your text below to analyze the angry level:")
    
    user_input = st.text_area("Input Text", "")
    
    if st.button("Analyze"):
        if user_input:
            sentiment = analyze_sentiment(user_input)
            angry_level = get_angry_level(sentiment)
            st.write("Sentiment Score:", sentiment)
            st.write("Angry Level:", angry_level)

if __name__ == "__main__":
    main()
