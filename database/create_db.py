import sqlite3
def create_database():
    conn = sqlite3.connect('my_proyect.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY, name TEXT)''')
    conn.commit()
    conn.close()
if __name__ == "__main__":
    create_database()
