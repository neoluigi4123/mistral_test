import config
import llm

assistant = llm.llm(model=config.DEFAULT_MODEL)
while True:
    prompt = input("> ")
    
    response = assistant.generate(prompt)

    print(f"assistant:\n{response}")