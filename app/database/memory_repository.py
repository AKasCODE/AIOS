from app.database.database import get_connection
from app.core.prompts import MEMORY_EXTRACTION_PROMPT

def save_memory(memory: str):
    conn=get_connection()
    curr=conn.cursor()
    curr.execute("INSERT INTO long_term_memory (memory) VALUES(?)",(memory,))
    conn.commit()
    conn.close()

def get_all_memories():
    conn=get_connection()
    curr=conn.cursor()
    curr.execute("SELECT memory FROM long_term_memory")
    memory = curr.fetchall()
    conn.close()
    return [i[0] for i in memory]