import random
import string
import hashlib
import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('password_manager.db')
cursor = conn.cursor()

# Create the passwords table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 account TEXT NOT NULL,
                 salt TEXT NOT NULL,
                 hashed TEXT NOT NULL)''')
conn.commit()

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def hash_password(password, salt):
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
    return hashed

def save_password(account, password):
    salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    hashed = hash_password(password, salt)
    cursor.execute('INSERT INTO passwords (account, salt, hashed) VALUES (?, ?, ?)', (account, salt, hashed))
    conn.commit()

def verify_password(account, password):
    cursor.execute('SELECT salt, hashed FROM passwords WHERE account = ?', (account,))
    result = cursor.fetchone()

    if result:
        salt, hashed_stored = result
        hashed_input = hash_password(password, salt)
        return hashed_stored == hashed_input

    return False

if __name__ == "__main__":
    print("Welcome to the Secure Password Manager!")

    while True:
        print("\nMenu:")
        print("1. Generate Password")
        print("2. Store Password")
        print("3. Verify Password")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            password_length = int(input("Enter the desired password length: "))
            new_password = generate_password(password_length)
            print("Generated Password:", new_password)
        
        elif choice == "2":
            account = input("Enter the account name: ")
            password = input("Enter the password: ")
            save_password(account, password)
            print("Password saved successfully!")
        
        elif choice == "3":
            account = input("Enter the account name: ")
            password = input("Enter the password: ")
            if verify_password(account, password):
                print("Password is correct.")
            else:
                print("Password is incorrect or account does not exist.")
        
        elif choice == "4":
            print("Exiting Secure Password Manager.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

    conn.close()
