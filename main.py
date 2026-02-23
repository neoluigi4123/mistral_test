import config
import llm
import json

assistant = llm.llm(model=config.DEFAULT_MODEL)
try:
    with open("local_data/context.json", "r") as file:
        previous_context = json.load(file)
except Exception as e:
    print(f"Error reading context: {e}")

while True:
    prompt = input("> ")
    
    response = assistant.generate(prompt)

    print(f"assistant:\n{response}")