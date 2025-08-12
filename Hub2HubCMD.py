from image2key import image2key
import os
import sqlite3

conn = sqlite3.connect("file_database.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filepath TEXT NOT NULL,
        filesize INTEGER NOT NULL,
        key TEXT NOT NULL,
        tags TEXT
    )
''')
conn.commit()

def new_file_record(filepath, tags):
    filesize = os.path.getsize(filepath)
    key = image2key("dog.png")
    tags_string = ",".join(tags)

    cursor.execute('INSERT INTO files (filepath, filesize, key, tags) VALUES (?, ?, ?, ?)',
                (filepath, filesize, key, tags_string))
    conn.commit()


new_file_record("dog.png", ["dog", "cute"])