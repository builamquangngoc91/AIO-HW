import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

st.title('Chatbot')

with st.sidebar:
    st.write('Huggingface Account')
    hf_email = st.text_input('Email')
    hf_password = st.text_input('Password', type='password')

if 'messages' not in st.session_state.keys():
    st.session_state.messages = [{'role': 'assistant', 'content': 'How may I help you'}]

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])

def generate_response(prompt_input, email, password):
    sign = Login(email, password)
    cookies = sign.login()

    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

if prompt := st.chat_input(disabled=not(hf_email and hf_password)):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.write(prompt)

if st.session_state.messages[-1]['role'] != 'assistant':
    with st.chat_message('assistant'):
        with st.spinner('Thinking...'):
            response = generate_response(prompt, hf_email, hf_password)
            st.write(response)
    message = {'role': 'assistant', 'content': response}
    st.session_state.messages.append(message)