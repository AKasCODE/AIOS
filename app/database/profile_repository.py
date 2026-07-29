from app.database.database import get_connection

def save_profile(key:str, value:str):
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
    INSERT INTO user_profile (key,value) VALUES (?,?)
    ON CONFLICT(key)
    DO UPDATE SET value = excluded.value;
    """,(key,value))
    conn.commit()
    conn.close()

def get_profile():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("SELECT key, value FROM user_profile")
    rows = curr.fetchall()
    conn.close()
    return {key: value for key, value in rows}

