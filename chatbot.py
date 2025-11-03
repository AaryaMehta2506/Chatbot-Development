import requests
import json

API_URL = "http://localhost:11434/api/chat"

def query_ollama(prompt):
    payload = {
        "model": "phi3:mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        data = response.json()
        return data["message"]["content"].strip()
    else:
        return f"Error {response.status_code}: {response.text}"

def chat():
    print("Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = query_ollama(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
