import config
from mistralai import Mistral

class llm:
    def __init__(self, model: str, api_key: str = config.MISTRAL_API_KEY):
        self.model = model
        self.client = Mistral(api_key=api_key)
    
    def generate(self, prompt):
        chat_response = self.client.chat.complete(
            model = self.model,
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )
        return chat_response.choices[0].message.content