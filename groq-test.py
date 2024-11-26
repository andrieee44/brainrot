import os

from groq import Groq
from openai import OpenAI

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "message": "You will be writing a narration based on this text",
        },
        {
            "role": "user",
            "content": "Im just a chill guy",
        }
    ],
    model="llama-3.2-90b-vision-preview",
)

print(chat_completion.choices[0].message.content)