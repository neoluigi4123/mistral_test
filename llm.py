"""
This module defines the llm class, which serves as a wrapper around the Mistral API for generating responses based on prompts. It provides a simple interface for interacting with the Mistral language model.
"""
import config
from typing import Any
from mistralai import Mistral

class llm:
    def __init__(self, model: str, api_key: str = config.MISTRAL_API_KEY):
        self.model = model
        self.client = Mistral(api_key=api_key)
        self.context: list[Any] = [
            {
                "role": "system",
                "content": "You are a helpful assistant that provides accurate and concise information to the user.",
            }
        ]

    def generate(self, prompt: str):
        """Generates a response from the LLM based on the given prompt.
        Args:
            prompt (str): The input prompt to generate a response for.
        Returns:
            str: The generated response from the LLM.
        """
        self.add_to_context(prompt)
        chat_response = self.client.chat.complete(
            model = self.model,
            messages = self.context
        )
        self.add_to_context(str(chat_response.choices[0].message.content), "assistant")
        return chat_response.choices[0].message.content

    def add_to_context(self, content: str, role: str = 'user') -> None:
        """Adds contents to the context.
        Args:
            role (str): the role of the message(can be: "user","system","assistant").
            content (str): the content of the message.
        Returns:
            None.
        """
        self.context.append({
            "role": role,
            "content": content
        })

if __name__ == "__main__":
    assistant = llm(model=config.DEFAULT_MODEL)
    response = assistant.generate("What is the capital of France?")
    print(response)