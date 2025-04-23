import openai
from dotenv import load_dotenv
import os

load_dotenv()
# Set your OpenAI API key
API_KEY = os.getenv("API_KEY")

client = openai.OpenAI(api_key = API_KEY)
print(client)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")