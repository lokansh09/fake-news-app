import sqlite3

# Connect or create new users.db
conn = sqlite3.connect("users.db")

# Read SQL from users.sql
with open("users.sql", "r") as f:
    sql_script = f.read()

# Execute the SQL to create the table
conn.executescript(sql_script)
conn.commit()
conn.close()

print("✅ users.db created and users table initialized.")
