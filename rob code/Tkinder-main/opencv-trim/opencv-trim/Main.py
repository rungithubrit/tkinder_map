import tkinter as tk
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect('user_credentials.db')
cursor = conn.cursor()

# Create 'users' table with columns for username and password
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
''')

# Function to register a new user
def register_user():
    username = entry_reg_username.get()
    password = entry_reg_password.get()

    
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Registration", "Registration successful!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Registration", "Username already exists. Please choose a different username.")

    conn.close()

# Function to authenticate user
def authenticate():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect('user_credentials.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        messagebox.showinfo("Login", "Authentication successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login and Registration")

# Registration Form
label_reg_username = tk.Label(root, text="Register - Username:")
label_reg_username.pack()
entry_reg_username = tk.Entry(root)
entry_reg_username.pack()

label_reg_password = tk.Label(root, text="Register - Password:")
label_reg_password.pack()
entry_reg_password = tk.Entry(root, show="*")  # 'show' attribute hides password input
entry_reg_password.pack()

register_button = tk.Button(root, text="Register", command=register_user)
register_button.pack()

# Login Form
label_username = tk.Label(root, text="Login - Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Login - Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")  # 'show' attribute hides password input
entry_password.pack()

login_button = tk.Button(root, text="Login", command=authenticate)
login_button.pack()

# Run the application
root.mainloop()
