# imagine we are working on a program where the user needs to enters data to sign up for a website. 
# Fill out the get_user_data() function which:

# Asks the user for their first name and stores it in a variable

# Asks the user for their last name and stores it in a variable

# Asks the user for their email address and stores it in a variable

# Returns all three of these pieces of data in the order it was asked

def get_user_data():
    """ Prompts the user for their first name, last name, and email address. """
    first_name = input("What is your first name?: ")  # Ask for first name
    last_name = input("What is your last name?: ")    # Ask for last name
    email = input("What is your email address?: ")      # Ask for email address
    
    return first_name, last_name, email  # Return all three pieces of data as a tuple

def main():
    user_data = get_user_data()  # Call the function to get user data
    print(f"Received the following user data: {user_data}")  # Print the received data

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()