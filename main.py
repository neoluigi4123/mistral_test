"""
This is the main entry point for the application. It initializes the assistant, loads any previous context, and enters a loop to interact with the user.
"""
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
    for msg in previous_context[1:]:
        assistant.add_to_context(msg['content'], msg['role'])
else:
    print("No previous context found. Starting fresh...")

while True:
    prompt = input("> ")
    if prompt.startswith("/clear"):
        print("clearing context...")
        assistant.context = [{
            "role": "system",
            "content": config.SYSTEM_PROMPT
        }]

    if prompt.startswith("/exit") or prompt.startswith("/bye"):
        print("exiting...")
        break
    response = assistant.generate(prompt)

    print(f"assistant:\n{response}")