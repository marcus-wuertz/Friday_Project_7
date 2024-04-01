from tkinter import *
from tkinter import ttk
import sqlite3

def login():
    # Retrieve data from entry fields
    email = emailEntry.get()
    password = pwdEntry.get()

    # Connect to the SQLite database
    conn = sqlite3.connect('user_info.db')
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve the email and password for the provided email
    cursor.execute("SELECT email, password FROM login_info WHERE email=?", (email,))
    user_data = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # If user_data is not None and the password matches, login was successful
    if user_data and user_data[0] == email and user_data[1] == password:
        print("Login successful!")
    else:
        print("Error: Invalid email or password. Please try again.")

# establish the parent
root=Tk()
root.title('Login page')

# welcome message
greeting= ttk.Label(root, text='Returning user? Login here!', font=('TkDefaultFont', 20))
greeting.grid(column=2)

# create a label for email
emailLbl= ttk.Label(root, text='Email',font=(16))
emailLbl.grid(row=1, column=0)

# create an entry box for email
emailEntry=ttk.Entry(root)
emailEntry.grid(row=1, column=2, sticky='ew')

# create a label for Password
pwdLbl= ttk.Label(root, text='Password',font=(16))
pwdLbl.grid(row=2, column=0)

# create an entry box for Password
pwdEntry=ttk.Entry(root, show="*")
pwdEntry.grid(row=2, column=2, sticky='ew')

# create a login button
loginBtn=ttk.Button(root, text='Login', command=login)
loginBtn.grid(row=3, column=2)
root.mainloop()