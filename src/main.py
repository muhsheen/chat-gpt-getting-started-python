import os
import dotenv
import openai

dotenv.load_dotenv()

openai.api_key = os.environ.get("OPEN_AI_KEY")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "what is the fastest land animal?"}]
)

messages = ", ".join(list(map(lambda choice: choice.message.content, completion.choices)))
print(messages)
