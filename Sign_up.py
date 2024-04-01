from tkinter import *
from tkinter import ttk
import sqlite3 

# establish function to insert data into database
def sign_up():
    # Retrieve data from entry fields
    first_name = nameEntry1.get()
    last_name = nameEntry2.get()
    username = userNameEntry.get()
    email = emailEntry.get()
    password = pswdEntry1.get()
    reenter_password = pswdEntry2.get()

    if password != reenter_password:
        print("Error: Passwords do not match. Please try again.")
        return  # Exit the function if passwords don't match
    
    # Check if email follows the correct format
    if '@' not in email or not email.endswith('.com'):
        print("Error: Invalid email format. Please enter a valid email address.")
        return  # Exit the function if email format is invalid

    # Insert data into the database
    conn = sqlite3.connect('user_info.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO login_info (first_name, last_name, username, email, password, reenter) VALUES (?, ?, ?, ?, ?, ?)",
                   (first_name, last_name, username, email, password, reenter_password))
    conn.commit()

    # Check if the data has been successfully inserted
    cursor.execute("SELECT * FROM login_info WHERE first_name=? AND last_name=? AND username=? AND email=? AND password=? AND reenter=?",
                   (first_name, last_name, username, email, password, reenter_password))
    user_data = cursor.fetchone()
    conn.close()

    # If user_data is not None, insertion was successful
    if user_data:
        print("Sign-up successful!")
    else:
        print("Error: Sign-up failed. Please try again.")

#establish parent
root=Tk()
root.title("Sign up page")

# create widget for welcome message
label1= ttk.Label(root, text='New? Create an account!', font=('TkDefaultFont',20))
label1.grid(column=2)

# create label and entry box for first name
nameLbl1= ttk.Label(root, text='First Name', font=('TkDefaultFont',16))
nameLbl1.grid(row=1, column=0)

nameEntry1=ttk.Entry(root)
nameEntry1.grid(row=1,column=2, sticky='ew')

# create labels and entry boxes for last name
nameLbl2= ttk.Label(root, text='Last Name', font=('TkDefaultFont',16))
nameLbl2.grid(row=2, column=0)

nameEntry2=ttk.Entry(root)
nameEntry2.grid(row=2,column=2, sticky='ew')

# create label and entry box for username
userNameLbl= ttk.Label(root, text='Username', font=('TkDefaultFont',16))
userNameLbl.grid(row=3, column=0)

userNameEntry=ttk.Entry(root)
userNameEntry.grid(row=3,column=2, sticky="ew")

# create label and entry box for email
emailLbl= ttk.Label(root, text='Email', font=('TkDefaultFont',16))
emailLbl.grid(row=4, column=0)

emailEntry=ttk.Entry(root)
emailEntry.grid(row=4,column=2, sticky="ew")

# create label and entry box for password
pswdLbl1= ttk.Label(root, text='Password', font=('TkDefaultFont',16))
pswdLbl1.grid(row=5, column=0)

pswdEntry1=ttk.Entry(root, show="*")
pswdEntry1.grid(row=5,column=2, sticky="ew")

# create label and entry box for reenter password
pswdLbl2= ttk.Label(root, text='Reenter Password', font=('TkDefaultFont',16))
pswdLbl2.grid(row=6, column=0)

pswdEntry2=ttk.Entry(root, show="*")
pswdEntry2.grid(row=6,column=2, sticky="ew")

# create a button to submit form
btn1= ttk.Button(root, text='Sign up now', command=sign_up)
btn1.grid(row=7,column=2)

root.mainloop()