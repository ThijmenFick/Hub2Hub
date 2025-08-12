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

def precheck_record(filepath, threshold):
    new_key = image2key(filepath)

    cursor.execute("SELECT key FROM files")
    rows = cursor.fetchall()
    keys = [row[0] for row in rows]

    all_matches = []

    for key in keys:
        matches = 0
        total = len(new_key)

        for c1, c2 in zip(new_key, key):
            if c1 == c2:
                matches += 1

        if (matches / total) * 100 > threshold:
            all_matches.append(key)

    if len(all_matches) == 0:
        print("No matches found")
    else:
        print(f"{len(all_matches)} match(es) found")

#new_file_record("dog.png", ["dog", "cute"])
#precheck_record("dog.png", 70)