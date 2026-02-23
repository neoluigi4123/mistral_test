import config
from mistralai import Mistral

api_key = config.MISTRAL_API_KEY
model = "mistral-large-latest"

client = Mistral(api_key=api_key)
class llm:
    def __init__(self):
        pass
    
    def generate(self, prompt):
        chat_response = client.chat.complete(
            model = model,
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )
        return chat_response.choices[0].message.content