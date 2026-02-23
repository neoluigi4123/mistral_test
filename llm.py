"""
This module defines the llm class, which serves as a wrapper around the Mistral API for generating responses based on prompts. It provides a simple interface for interacting with the Mistral language model.
"""
import config
import json
import os
import websearch
from typing import Any, Dict
from mistralai import Mistral
from mistralai.models import Tool, Function 

webSearchTool = [
    Tool(
        type="function",
        function=Function(
            name="retrieve_web_search_results",
            description="Get web search results for a query",
            parameters={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The web search query.",
                    }
                },
                "required": ["query"],
            },
        )
    )
]

class llm:
    def __init__(self, model: str, api_key: str = str(config.MISTRAL_API_KEY)):
        self.model = model
        self.client = Mistral(api_key=api_key)
        self.context: list[Any] = [
            {
                "role": "system",
                "content": config.SYSTEM_PROMPT,
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
        
        result = None
        
        # Loop until we get a result that has text content
        while not result or not result.content:
            chat_response = self.client.chat.complete(
                model = self.model,
                messages = self.context,
                tools = webSearchTool,
                tool_choice = "auto"  # 'auto' lets the model decide when to answer or use a tool
            )
            result = chat_response.choices[0].message
            
            if result.tool_calls:
                for tool_call in result.tool_calls:
                    if tool_call.function.name == "retrieve_web_search_results":
                        args = json.loads(tool_call.function.arguments)
                        query = args.get("query", "")
                        
                        search_results = websearch.web(query)
                        
                        # Feed the results back as "user" so the model reads the new information
                        self.add_to_context(f"Web search results for '{query}': {search_results}", "tool")
            
            elif result.content:
                self.add_to_context(result.content, "assistant")
                return result.content

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
        try:
            directory = os.path.dirname("local_data/context.json")
            os.makedirs(directory, exist_ok=True)
            with open("local_data/context.json", "w", encoding="utf-8") as f:
                json.dump(self.context, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving context: {e}")

if __name__ == "__main__":
    assistant = llm(model=config.DEFAULT_MODEL)
    response = assistant.generate("When's the release of the movie in 2026 of the Super Mario Bros the movie 2 aka mario galaxy the movie?")
    print(response)
    print(f"context:\n{assistant.context}")