from app.database.database import get_connection

def save_message(role, content):
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("INSERT INTO conversation (role, content) VALUES (?, ?)",(role, content))
    conn.commit()
    conn.close()

def get_recent_messages(limit:int =20):
    conn = get_connection()
    curr= conn.cursor()
    curr.execute("SELECT role, content FROM conversation ORDER BY id DESC LIMIT ?",(limit,))
    rows= curr.fetchall()
    rows.reverse()
    conn.close()
    return [{"role":row[0], "content":row[1]} for row in rows ]
