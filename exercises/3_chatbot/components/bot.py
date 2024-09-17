from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

EDEN_API_KEY = os.getenv("EDEN_API_KEY")

class Bot:
    def __init__(self) -> None:
        self._history = []

    def chat(self, prompt):
        headers = {"Authorization": f"Bearer {EDEN_API_KEY}"}

        url = "https://api.edenai.run/v2/text/chat"
        payload = {
            "providers": "openai/gpt-40-mini",
            "text": prompt,
            "chatbot_global_action": """You are a cranky old man. Your name is Sylvester and you don't like it when people ask stupid questions. 
            If people do teach them a lesson.""",
            "previous_history": self._history,
            "temperature": 0.5,
            "max_tokens": 150
        }

        response = requests.post(url, json=payload, headers=headers)
        answer = json.loads(response.text)["openai/gpt-40-mini"]["generated_text"]

        self._history.append({"role": "user", "message": prompt})
        self._history.append({"role": "assistent","message": answer})

        return answer