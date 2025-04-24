# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, 
# and an integer repeats number of times to print message. We've written the main() function for you, 
# which prompts the user for a message and a number of repeats.

def print_multiple(message, repeats):
    for _ in range(repeats):  # Loop for the number of repeats
        print(message, end=' ')  # Print the message without a newline
    print()  # Print a newline at the end

def main():
    message = input("Please type a message: ")  # Prompt for a message
    user_input = input("Enter a number of times to repeat your message: ")
    try:
        repeats = int(user_input)  # Convert input to an integer
        print_multiple(message, repeats)  # Call the function to print the message
    except ValueError:
        print("Please enter a valid integer.")  # Handle invalid input

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()