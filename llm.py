import os
import config
from mistralai import Mistral

api_key = config.MISTRAL_API_KEY
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def generate():
    chat_response = client.chat.complete(
        model = model,
        messages = [
            {
                "role": "user",
                "content": "Tell me a joke.",
            },
        ]
    )
    return chat_response.choices[0].message.content