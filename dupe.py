import streamlit as st
import requests

import pandas as pd
df = pd.read_csv(r"C:\Users\flypbox\Desktop\time table sem 4.csv")
data_text = df.to_string()


# Ollama API URL
URL = "http://localhost:11434/api/generate"

st.set_page_config(page_title="Ollama Chat", layout="centered")

st.title("🤖 Local Chatbot (Ollama)")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)

    # Send request to Ollama
    data = {
    "model": "gemma:2b",
    "prompt": f"""
You are a data assistant.

Here is the dataset:
{data_text}

Answer this question based only on the dataset:
{user_input}

Give short answers.
""",
    "stream": False
}

    response = requests.post(URL, json=data)
    reply = response.json()["response"]

    # Show bot reply
    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})