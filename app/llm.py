import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY environment variable not set. Please add it to your .env file")


client = OpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1")

def ask_llm(prompt: str) -> str:

    response = client.chat.completions.create(
        model="openai/gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000

    )
    return response.choices[0].message.content
