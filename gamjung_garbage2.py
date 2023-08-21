import streamlit as st
import random
import openai

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

# 공감 표현 목록
empathetic_responses = [
    "정말 손해를 입은 것 같아요.",
    "당신의 기분을 이해해요. 제가 이곳에 있어 대화를 나눌 준비가 되어 있어요.",
    # ... 나머지 공감 표현 추가 ...
]

def get_empathetic_response(user_message):
    # Generate a response using GPT-3
    prompt = f"User: {user_message}\nBot:"
    gpt_response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=50
    )
    return gpt_response.choices[0].text.strip()

# Streamlit 앱
def main():
    st.set_page_config(page_title="공감 대화 봇", page_icon="🌸")
    st.title("공감 대화 봇")
    st.markdown("### 이야기를 해주세요! 저는 여기 있어요. 🌈")
    
    user_messages = st.text_area("대화 내용", height=200, help="여기에 대화 내용을 입력하세요.")
    
    if st.button("대화 시작"):
        if not user_messages:
            st.warning("대화 내용을 입력해주세요.")
            return
        
        conversation = user_messages.split("\n")
        
        with st.spinner("봇이 생각하고 있어요..."):
            user_message = conversation[-1].replace("User:", "").strip()
            
            if user_message:
                bot_response = get_empathetic_response(user_message)
                conversation.append(f"User: {user_message}")
                conversation.append(f"Bot: {bot_response}")
                st.text("봇: " + bot_response)
            else:
                st.warning("사용자 메시지를 입력하세요.")
        
        st.text_area("대화 내용", "\n".join(conversation), height=200, disabled=True)

if __name__ == "__main__":
    main()
