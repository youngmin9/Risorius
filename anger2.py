import streamlit as st
from textblob import TextBlob
import random

# 감정 분류 및 대응 메시지
empathetic_responses = {
    "positive": [
        "정말 좋아요! 학생들의 성과에 기여하신 데 자부심을 가져야 해요.",
        "멋져요! 교육은 미래를 만드는 중요한 일이에요.",
        "기쁨이 느껴지네요! 학생들의 성공을 함께 나눠보세요."
    ],
    "neutral": [
        "그렇군요. 학생들의 상황을 더 자세히 알려주실 수 있나요?",
        "알겠습니다. 교육 분야에서의 경험을 들려주시겠어요?",
        "조금 더 자세한 이야기를 해보세요.",
        "학생들의 미래에 대한 걱정을 나누는 건 어떨까요?"
    ],
    "negative": [
        "어려운 일이 많이 있으셨겠군요. 어떤 상황에서 힘들게 느껴지나요?",
        "조금 힘들게 느껴질 수도 있어요. 제게 어떤 점이 어려우셨나요?",
        "마음이 무거우셨을 텐데, 함께 이야기해보는 건 어떨까요?",
        "학생들과의 소통이 힘들게 느껴지나요? 그 상황에 대해 얘기해보세요.",
        # ... (기존 응답들)
    ],
    "angry": [
        "화가 날 때는 이야기하면서 스트레스를 푸는 것도 좋아요.",
        "화가 날 수 있지만, 그래도 학생들에게 좋은 영향을 주려는 노력은 중요해요.",
        "화가 날 때는 학생들의 미래를 생각하며 힘을 내보세요.",
        "분노를 긍정적인 힘으로 바꾸어 학생들에게 좋은 영향을 줄 수 있어요."
    ],
    "work_stress": [
        "교육 분야에서 스트레스를 느끼셨다면, 동료들과 함께 이야기하며 해결책을 모색해보세요.",
        "학생들의 미래를 위해 열심히 하시는 것은 소중한 일이에요. 그러나 휴식도 필요해요.",
        "교육 분야에서 일하면서 생기는 스트레스를 관리하는 방법을 찾는 것이 중요해요.",
        "학생들과의 관계를 개선하며 교육 환경을 더 나아지게 만드는 노력이 필요해요."
    ]
}

def get_empathetic_response(user_message):
    blob = TextBlob(user_message)
    sentiment = blob.sentiment.polarity
    
    # 문맥을 고려하여 응답 선택
    if sentiment > 0.3:
        return random.choice(empathetic_responses["positive"])
    elif sentiment < -0.3:
        for context, keywords in empathetic_responses.items():
            if context != "positive":
                if any(keyword in user_message for keyword in keywords):
                    return random.choice(empathetic_responses[context])
        return random.choice(empathetic_responses["negative"])
    else:
        return random.choice(empathetic_responses["neutral"])

# Streamlit 앱
def main():
    st.set_page_config(page_title="교육 종사자 공감형 챗봇", page_icon="📚")
    st.title("교육 종사자 공감형 챗봇")
    
    user_message = st.text_input("대화 시작:")
    
    if user_message:
        bot_response = get_empathetic_response(user_message)
        st.text("당신: " + user_message)
        st.text("챗봇: " + bot_response)

if __name__ == "__main__":
    main()
