import streamlit as st
import requests
from typing import Generator
import os

api_base_url = os.environ.get('API_BASE_URL', 'http://simple-rag-server:10999')

st.title("北京旅游景点查询")

# 初始消息
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant",
            "content": "请提出有关北京景点的问题，目前包括：北海、恭王府、故宫、国博、景山、天坛、颐和园和八达岭。"}
    ]

# 显示输入框
if prompt := st.chat_input(placeholder="这里输入问题，换行请使用 Shift+Enter。"):
    st.session_state.messages.append(
        {"role": "user", "content": prompt})


# 显示之前的消息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if len(st.session_state.messages) > 0:
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):

            headers = {
                "Content-Type": "application/json",
                "accept": "text/event-stream"
            }
            response = requests.post(
                url=f"{api_base_url}/query",
                json={"query": prompt},
                headers=headers,
                stream=True,
            )

            response = st.write_stream(
                response.iter_content(decode_unicode=True))
            
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)