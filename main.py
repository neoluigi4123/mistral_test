import config
from llm import llm
import json

assistant = llm(model=config.DEFAULT_MODEL)

previous_context = None

# Load previous context if available
try:
    with open("local_data/context.json", "r") as file:
        previous_context = json.load(file)
except Exception as e:
    print(f"Error reading context: {e}")

if previous_context:
    print("Previous context loaded...")
    for messages in previous_context:
        assistant.add_to_context(messages["content"], messages["role"])
else:
    print("No previous context found. Starting fresh...")

while True:
    prompt = input("> ")
    
    response = assistant.generate(prompt)

    print(f"assistant:\n{response}")