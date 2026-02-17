import sqlite3

# Path to the users.sql file
sql_file_path = 'users.sql'  # Adjust the path if necessary

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Open the users.sql file
with open(sql_file_path, 'r') as f:
    sql_script = f.read()

# Execute the SQL commands to create the users table
cursor.executescript(sql_script)
conn.commit()

# Close the connection
conn.close()

print("Database created and initialized from users.sql")
