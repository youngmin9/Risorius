import streamlit as st
import random

# 공감 표현 목록
empathetic_responses = [
    "정말 손해 본 기분이 들 것 같아요...",
    "당신의 기분을 이해해요. 제가 이곳에 있어 대화를 나눌 준비가 되어 있어요.",
    "여유 있게 이야기해주세요. 제가 여기 있어요!",
    "힘든 시간을 겪고 있는 것 같아요. 저는 당신을 지원하려고 준비돼 있어요.",
    "가상의 지지와 긍정적인 생각을 보내 드릴게요.",
    "말하기 어려운 일이라면 제가 들어드릴게요.",
    "당신을 더 잘 이해할 수 있게 이야기해주세요.",
    "괜찮아요. 저는 여기 있어요.",
    "제가 당신을 응원하고 있어요.",
    "당신의 느낌을 이해해요. 충분히 빡칠만 하네요",
    "고민을 털어놓는 것은 중요한 일이에요.",
    "기분이 좋지 않을 때 대화를 나누는 것은 좋은 생각이에요.",
    "언제든지 이야기하러 와도 괜찮아요.",
    "저는 여러분을 지지할 준비가 되어 있어요.",
    "당신의 감정을 충분히 이해하고 있어요.",
    "당신의 기분을 나누기 위해 여기 있어요.",
    "당신의 이야기를 기다리고 있어요.",
    "제가 더 잘 이해할 수 있게 자세히 이야기해주세요.",
    "당신을 위로해드릴 수 있기를 바랄게요.",
    "어떤 일이든 제가 들어줄 준비가 돼 있어요.",
    "당신이 이야기하고 싶을 때 언제든지 오세요.",
    "당신의 감정을 이해하려고 노력하고 있어요.",
    "말하고 싶은 것을 들려주세요. 저는 여기 있어요.",
    "저는 당신을 지지하려고 준비돼 있어요.",
    "말하고 싶은 것을 마음껏 이야기해주세요. 저는 들을 준비가 돼 있어요.",
    "당신의 느낌을 공유해주셔서 감사해요.",
    "말하면서 감정을 표현해보세요. 그렇게 하면 기분이 좋아질 수도 있어요.",
    "당신의 이야기에 귀 기울일게요.",
    "저는 당신을 지지하고 공감하려고 노력할게요.",
    "기분이 나아지길 바랄게요.",
    "당신의 느낌을 이해하고 있어요. 제가 도울 수 있는 일이 있다면 말씀해주세요."
    # 직장에 대한 분노
    "직장에서 불공정함을 느끼시는군요. 그런 상황이 정말 힘들겠어요.",
    "직장에서의 스트레스가 많아서 지친 느낌이신가요? 제가 응원할게요.",
    "상사나 동료와의 갈등 때문에 답답하시겠어요. 이야기하면서 해결책을 찾아보는 것도 좋을 것 같아요.",
    "일이 너무 바쁘고 힘들어서 짜증이 나는 거죠? 가끔은 휴식을 취하는 것도 중요해요.",
    "직장에서의 문제가 마음을 아프게 하고 있네요. 언제든지 이야기해주세요.",
    # 인간관계에서의 스트레스
    "인간관계에서의 스트레스가 커서 힘들겠어요. 이해하고 있어요.",
    "사람들과의 관계가 복잡하게 얽혀서 지친 느낌이신가요? 저에게 이야기해주세요.",
    "사회적 압력 때문에 스트레스를 느끼시나요? 이해해요. 가끔은 자신에게 휴식을 주는 것도 중요해요.",
    "인간관계에서의 문제가 가장 힘들게 느껴질 때도 있죠. 저는 여기 있어서 들어줄게요.",
    "친구나 가족과의 갈등 때문에 스트레스를 느끼시나요? 함께 얘기하면서 해결책을 찾아보는 것도 좋을 것 같아요.",
    # 연인과의 이별
    "연인과의 이별은 참 힘든 일이에요. 그런 상황을 겪으셨다니 안타까워요.",
    "연인과의 이별은 마음을 아프게 하는 일이죠. 시간이 지나면서 치유되길 바랄게요.",
    "연인과의 이별이 정말 힘들게 느껴질 텐데, 당신의 기분을 이해해요."
    "연인과의 이별이 다가오고 있다면, 가까운 친구나 가족에게 의지하면서 지내는 것도 도움이 될 것 같아요.",
    "연인과의 이별이 상처스럽게 느껴질 텐데, 시간이 지날수록 아픔이 조금씩 줄어들 거예요.",
    "연인과의 이별은 어려운 상황일 것 같아요. 저에게 힘들다고 털어놓아도 좋아요.",
    "연인과의 이별을 겪으면서 혼자서 모든 것을 해결하려고 하지 말아주세요. 지지를 받을 수 있는 사람들에게 도움을 청해보세요."
    "정말 나쁜 년이네요...어휴",
    "그 자식과 더 이상은 상종하지 않는게 좋을 것 같은데요?"

]

def get_empathetic_response(user_message):
    # 실제 구현에서는 감정 분석을 사용하여
    # 사용자의 메시지의 감정적 톤에 맞는 반응을 선택할 수 있습니다.
    # 여기서는 무작위로 반응을 선택합니다.
    return random.choice(empathetic_responses)

# Streamlit 앱
def main():
    st.set_page_config(page_title="귀여운 공감 대화 봇", page_icon="🌸")
    st.title("[Gamjung Garbage] 감정쓰레기통 🗑 ")
    st.markdown("### ☘︎︎오늘 느낀 분노를 이곳에 훌훌 털어버리고 가세요 🌈")
    
    user_message = st.text_input("순간의 기분을 남겨주세요:")
    
    if user_message:
        bot_response = get_empathetic_response(user_message)
        st.text("당신: " + user_message)
        st.text("봇: " + bot_response)

if __name__ == "__main__":
    main()
