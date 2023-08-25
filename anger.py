import streamlit as st
import random

# 분노와 관련된 응답 목록
angry_responses = [
    "정말 손해 본 기분이 들 것 같아요...",
    "분노가 가득한 것 같네요. 제가 도와드릴 수 있는 게 있다면 얘기해주세요.",
    "화가 날 때는 이야기해보는 것도 도움이 될 수 있어요.",
    "힘들게 느껴지는군요. 어떤 일 때문에 힘들게 느껴지나요?",
    "스트레스가 많이 쌓인 것 같아요. 휴식을 취하는 것도 중요해요.",
    # ... (더 많은 분노 응답을 추가할 수 있습니다)
]

# Streamlit 앱
def main():
    st.set_page_config(page_title="분노 공감형 챗봇", page_icon="😡")
    st.title("분노 공감형 챗봇 😡")

    user_input = st.text_input("오늘 분노를 느낀 일을 알려주세요:")
    
    if user_input:
        # 입력 메시지에 분노와 관련된 키워드를 확인하여 응답 선택
        if any(keyword in user_input for keyword in ["분노", "화나","빡쳐"]):
            bot_response = random.choice(angry_responses)
        else:
            bot_response = "분노와 관련된 이야기를 들려주세요. 저는 여기 있어요."
        
        st.text("당신: " + user_input)
        st.text("챗봇: " + bot_response)

if __name__ == "__main__":
    main()
