import config
import llm

assistant = llm.llm(model=config.DEFAULT_MODEL)
while True:
    response = assistant.generate(input("> "))

    print("assistant:\n",response)