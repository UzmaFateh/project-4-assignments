# Enter a message to copy: Hello world!

# List before: []

# List after: ['Hello world!', 'Hello world!', 'Hello world!']


def add_three_copies(data_list, data):
    """Adds three copies of the data to the provided list."""
    for _ in range(3):
        data_list.append(data)  # Modify the list in place

def main():
    # Get user input
    user_input = input("Enter a message to copy: ")

    # Initialize an empty list
    message_list = []
    print("List before:", message_list)

    # Call the function to add three copies of the user input
    add_three_copies(message_list, user_input)

    # Print the modified list
    print("List after:", message_list)

# Run the program
if __name__ == "__main__":
    main()