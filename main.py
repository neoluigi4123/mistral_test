import config
import llm

assistant = llm.llm(model=config.DEFAULT_MODEL)
while True:
response = assistant.generate("What is the capital of France?")

print(response)