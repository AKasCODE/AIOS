from app.services.llm_service import extract_profile
from app.database.profile_repository import save_profile
from app.core.logger import logger
import json

def process_profile(user_message: str):
    response = extract_profile(user_message)
    if not response['success']:
        return
    print(repr(response["reply"]))

    profile = json.loads(response['reply'])
    for key,value in profile.items():
        save_profile(key.lower(), value) 
