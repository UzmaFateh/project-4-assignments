# You want to be safe online and use different passwords for different websites. However, 
# you are forgetful at times and want to make a program that can match which password belongs 
# to which website without storing the actual password!

import hashlib

def hash_password(password):
    """Hashes a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(stored_logins, email, password_to_check):
    """Checks if the hashed password matches the stored hash."""
    # Hash the password to check
    hashed_password = hash_password(password_to_check)
    
    # Check if the email exists and if the hashed password matches
    if email in stored_logins and stored_logins[email] == hashed_password:
        return True
    return False

def main():
    # Dictionary to store email and hashed passwords
    stored_logins = {}

    # Example of adding users
    stored_logins["user@example.com"] = hash_password("securepassword123")
    stored_logins["admin@example.com"] = hash_password("adminpassword456")

    # User login attempt
    email = input("Enter your email: ")
    password_to_check = input("Enter your password: ")

    if login(stored_logins, email, password_to_check):
        print("Login successful!")
    else:
        print("Login failed! Invalid email or password.")

# Run the program
if __name__ == "__main__":
    main()