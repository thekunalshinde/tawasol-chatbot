import streamlit as st
import requests

st.set_page_config(
    page_title="Tawasol Amal Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Tawasol Amal Testing Assistant")
st.caption("Ask me anything about testing Tawasol Amal CRM workflows")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if question := st.chat_input("Ask about any Tawasol Amal workflow..."):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "https://tawasol-chatbot.onrender.com/chat",
                    json={"question": question}
                )
                answer = response.json()["answer"]
            except:
                answer = "Could not connect to backend. Make sure FastAPI is running."
        st.write(answer)
    
    st.session_state.messages.append({"role": "assistant", "content": answer})