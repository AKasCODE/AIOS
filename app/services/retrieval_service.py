from app.database.memory_repository import get_all_memories

def retrieve_memories(query: str):
    memories = get_all_memories()
    query_words = query.lower().split()
    relevant_memories = []
    for memory in memories:
        memory_lower = memory.lower()
        if any(word in memory_lower for word in query_words):
            relevant_memories.append(memory)
    return relevant_memories