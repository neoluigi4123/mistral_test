import config
import llm

assistant = llm.llm(model="mistral-large-latest")

response = assistant.generate("What is the capital of France?")

print(response)