from openai import OpenAI
from app.core.config import OPENROUTER_API_KEY, MODEL_NAME, MAX_TOKENS, BASE_URL
from app.core.prompts import SYSTEM_PROMPT
from app.core.logger import logger

client = OpenAI(api_key=OPENROUTER_API_KEY, base_url=BASE_URL)


def ask_llm(prompt: str):
    try:
        logger.info("Sending request to OpenRouter")
        response = client.chat.completions.create(
            model = MODEL_NAME,
            messages=[{"role": "system","content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}],max_tokens=MAX_TOKENS
                    )
        logger.info("Response received successfully")
        return {"success": True,
                "reply":response.choices[0].message.content}
    except Exception as e:
        logger.exception("Error while communicating with OpenRouter")
        return {"success":False,
                "error":str(e)}