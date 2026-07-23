from dotenv import load_dotenv
import os
load_dotenv("app/.env")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL_NAME = "deepseek/deepseek-chat-v3-0324"
        # qwen/qwen3-235b-a22b
MAX_TOKENS = 500
BASE_URL = "https://openrouter.ai/api/v1" 

#Instead of loading .env in every file, we load it once.