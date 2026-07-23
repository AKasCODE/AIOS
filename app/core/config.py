from dotenv import load_dotenv
import os
load_dotenv("app/.env")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
#Instead of loading .env in every file, we load it once.