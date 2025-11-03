import streamlit as st
import requests
import json

API_URL = "http://localhost:11434/api/chat"

def query_ollama(prompt):
    payload = {
        "model": "phi3:mini",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        data = response.json()
        return data["message"]["content"].strip()
    else:
        return f"Error {response.status_code}: {response.text}"

st.set_page_config(page_title="AI Chatbot")
st.title("Local AI Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask something:")

if st.button("Send") and user_input:
    response = query_ollama(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

for role, text in st.session_state.history:
    if role == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Bot:** {text}")
