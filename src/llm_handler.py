import os
from openai import OpenAI

API_TOKEN = os.getenv("AIPROXY_TOKEN")

def call_llm(prompt: str) -> str:
    client = OpenAI(api_key=API_TOKEN)
    response = client.Completions.create(model="gpt-4o-mini", prompt=prompt, max_tokens=50)
    return response.choices[0].text.strip()
