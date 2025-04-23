# Write a program which continuously asks the user to enter values which are added 
# one by one into a list. When the user presses enter without typing anything, print the list.

def main():
    # Initialize an empty list to store user inputs
    user_list = []

    while True:
        # Prompt the user to enter a value
        value = input("Enter a value:  ")
        
        # Check if the input is empty (user pressed Enter)
        if value == "":
            break  # Exit the loop if no input is provided
        
        # Add the entered value to the list
        user_list.append(value)

    # Print the final list
    print("Here's the list:", user_list)

# Run the program
if __name__ == "__main__":
    main()