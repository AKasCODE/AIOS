from app.services.conversation_service import add_user_message, add_assistant_message, get_recent_history
from app.services.llm_service import ask_llm
from app.services.profile_service import process_profile
from app.services.memory_service import process_memory
from app.database.profile_repository import get_profile
from app.services.retrieval_service import retrieve_memories
from app.core.prompts import SYSTEM_PROMPT

def process_chat(user_message: str):
    add_user_message(user_message)
    process_profile(user_message)
    process_memory(user_message)
    history = get_recent_history()
    profile = get_profile()
    memories = retrieve_memories(user_message)

    system_message =f"""{SYSTEM_PROMPT}
    
    USER PROFILE:
    {profile}

    Relevant Memories:
    {memories}"""

    messages = [{'role':'system', 'content':system_message},
                *history]
    response = ask_llm(messages)
    if response["success"]:
        add_assistant_message(response["reply"])
    return response