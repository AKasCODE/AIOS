from app.services.conversation_service import add_user_message, add_assistant_message, get_recent_history
from app.services.llm_service import ask_llm
from app.core.prompts import SYSTEM_PROMPT

def process_chat(user_message: str):
    add_user_message(user_message)
    history = get_recent_history()
    messages = [{'role':'system', 'content':SYSTEM_PROMPT},
                *history]
    response = ask_llm(messages)
    if response["success"]:
        add_assistant_message(response["reply"])
    return response