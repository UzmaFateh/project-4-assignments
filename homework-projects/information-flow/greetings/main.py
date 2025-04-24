# We've written a helper function for you called greet(name) which takes as input a string name and prints '
# 'a greeting. Write some code in main() to get the user's name and then greet them, being sure to call t
# he greet(name) helper function.

def greet(name):
    print(f"Greetings {name}!")  # Print a greeting with the provided name

def main():
    user_input = input("What's your name? ")  # Prompt for the user's name
    greet(user_input)  # Call the greet function with the user's name

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()