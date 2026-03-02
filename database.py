import sqlite3

DB_PATH = "north.db"
N = 250

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_message(role, message):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chats (role, message) VALUES (?, ?)", (role, message))
    conn.commit()
    conn.close()

def get_last_n_messages():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT role, message FROM chats ORDER BY id DESC LIMIT ?", (N,))
    rows = cursor.fetchall()
    conn.close()
    messages = []
    for row in rows:
        msg = {
            "role": row[0],
            "message": row[1]
        }
        messages.append(msg)
    messages.reverse()
    return messages

def get_all_messages():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT role, message FROM chats ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    messages = []
    i = 1
    for row in rows:
        if (i%2 == 0):
            message = row[1] + "\n"
        else:
            message = row[1]
        
        i += 1
        msg = {
            "role": row[0],
            "message": message
        }
        messages.append(msg)
    return messages

def delete_chats():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chats")
    conn.commit()
    conn.close()