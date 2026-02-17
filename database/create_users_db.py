import sqlite3

# ✅ Corrected path: saves 'users.db' in the current folder
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Drop the table if needed (for re-run safety)
cursor.execute("DROP TABLE IF EXISTS users")

# Create the users table
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
print("✅ users.db created successfully!")
