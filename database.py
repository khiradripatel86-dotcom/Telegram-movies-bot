import sqlite3

conn = sqlite3.connect("movies.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
name TEXT,
file_id TEXT
)
""")

conn.commit()

def add_movie(name,file_id):
    cursor.execute("INSERT INTO movies VALUES (?,?)",(name,file_id))
    conn.commit()

def get_movie(name):
    cursor.execute("SELECT file_id FROM movies WHERE name LIKE ?",('%'+name+'%',))
    return cursor.fetchone()
