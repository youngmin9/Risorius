https://github.com/youngmin9/Risorius/blob/master/anger4.pyimport streamlit as st
from textblob import TextBlob
import random

# 분노 레벨을 기반으로 한 응답 데이터셋
angry_responses = [
    "조금 더 차분하게 이야기해주세요.",
    "화를 내시면 안 돼요. 함께 해결해보아요.",
    "이해해요. 분노를 조금 진정시키고 대화해봐요.",
    "무슨 일이 있었나요? 제게 말해보세요.",
    "분노하실 이유가 충분한 것 같아요. 먼저 털어놓아보세요.",
    "화가 나신다면 호흡을 깊게 해보세요. 함께 해결해보아요."
]

def get_empathetic_response(user_message):
    blob = TextBlob(user_message)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.3:
        return "정말 좋아요! 기분 좋은 일이 있었나요?"
    elif sentiment < 0.3:
        return random.choice(angry_responses)
    else:
        return "그렇군요. 다른 얘기하고 싶은 주제가 있나요?"

# Streamlit 앱
def main():
    st.set_page_config(page_title="분노 감정 공감 봇", page_icon="😡")
    st.title("분노 감정 공감 봇")
    st.markdown("분노를 느끼고 계신가요? 이곳에서 털어놓아보세요.")

    user_message = st.text_input("분노를 느낀 내용을 입력하세요:")

    if user_message:
        bot_response = get_empathetic_response(user_message)
        st.text("당신: " + user_message)
        st.text("봇: " + bot_response)

if __name__ == "__main__":
    main()
