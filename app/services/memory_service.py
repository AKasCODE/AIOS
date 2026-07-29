import json

from app.database.memory_repository import save_memory
from app.services.llm_service import extract_memory


def process_memory(user_message: str):
    response = extract_memory(user_message)
    if not response["success"]:
        return
    reply = response["reply"]
    reply = reply.replace("```json", "")
    reply = reply.replace("```", "")
    reply = reply.strip()
    memory = json.loads(reply)
    if not memory:
        return
    save_memory(memory["memory"])