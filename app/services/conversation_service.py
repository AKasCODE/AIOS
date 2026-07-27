from app.database.conversation_repository import save_message, get_recent_messages

def add_user_message(message : str) -> None:
    save_message('user',message)

def add_assistant_message(message : str) -> None:
    save_message('assistant',message)

def get_recent_history():
    return get_recent_messages()

# history = get_recent_history()