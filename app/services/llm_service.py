from openai import OpenAI
from app.core.config import OPENROUTER_API_KEY, MODEL_NAME, MAX_TOKENS, BASE_URL
from app.core.prompts import SYSTEM_PROMPT, PROFILE_EXTRACTION_PROMPT, MEMORY_EXTRACTION_PROMPT
from app.core.logger import logger

client = OpenAI(api_key=OPENROUTER_API_KEY, base_url=BASE_URL)


def ask_llm(messages: list):
    try:
        logger.info("Sending request to OpenRouter")
        response = client.chat.completions.create(
            model = MODEL_NAME,
            messages=messages,
            max_tokens=MAX_TOKENS
                    )
        logger.info("Response received successfully")
        return {"success": True,
                "reply":response.choices[0].message.content}
    except Exception as e:
        logger.exception("Error while communicating with OpenRouter")
        return {"success":False,
                "error":str(e)}

def extract_profile(user_message: str):
    try:
        logger.info("Extracting profile information")
        response = client.chat.completions.create(
            model = MODEL_NAME,
            messages = [{'role':'system', 'content':PROFILE_EXTRACTION_PROMPT},
                        {'role':'user', 'content':user_message}],
            max_tokens = MAX_TOKENS
        )
        logger.info("Profile extraction successful")
        return {'success':True, 'reply':response.choices[0].message.content}
    except Exception as e:
        logger.exception("Profile extraction failed")
        return {'success':False, 'error':str(e)}

def extract_memory(user_message: str):
    try:
        logger.info("Extracting memory indormation")
        response = client.chat.completions.create(
            model = MODEL_NAME,
            messages = [{'role':'system', 'content':MEMORY_EXTRACTION_PROMPT},
                        {'role':'user', 'content':user_message}],
            max_tokens = MAX_TOKENS
        )
        logger.info("Memory extraction successful")
        return {'success':True, 'reply':response.choices[0].message.content}
    except Exception as e:
        logger.exception("Memory extraction failed")
        return {'success':False, 'error':str(e)}