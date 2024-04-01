import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('user_info.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define SQL command to create a table to hold user login information
cursor.execute('''CREATE TABLE IF NOT EXISTS login_info (
                    first_name TEXT,
                    last_name TEXT,
                    username TEXT,
                    email TEXT,
                    password TEXT,
                    reenter TEXT
                )''')


# # Execute a SELECT query to retrieve all rows from the 'login_info' table
# cursor.execute("SELECT * FROM login_info")

# # Print each row
# for row in cursor.fetchall():
#     print(row)

# # Close the cursor and connection
# cursor.close()
# conn.close()