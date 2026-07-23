from openai import OpenAI
from ..core.config import OPENROUTER_API_KEY

client = OpenAI(api_key=OPENROUTER_API_KEY, base_url="https://openrouter.ai/api/v1")
        # qwen/qwen3-235b-a22b


def ask_llm(prompt: str):
    response = client.chat.completions.create(
        model = "deepseek/deepseek-chat-v3-0324",
        messages=[{"role": "user", "content": prompt}],max_tokens=500
    )
    return response.choices[0].message.content