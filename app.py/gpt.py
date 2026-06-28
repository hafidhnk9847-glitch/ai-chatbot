import streamlit as st
from groq import Groq

client = Groq(api_key="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")

st.set_page_config(page_title="My AI Chatbot", page_icon="🤖", layout="centered")
st.title("My AI Chatbot")
st.markdown("### Ask me anything!")
st.divider()

with st.sidebar:
    st.header("About")
    st.write("Built by Hafidh")
    st.write("Powered by Groq")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )
    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
