# show an example of using dictionaries to keep track of information in a phonebook.

def main():
    # Initialize an empty dictionary to store the phonebook
    phonebook = {}

    while True:
        print("\nPhonebook Menu:")
        print("1. Add a contact")
        print("2. Search for a contact")
        print("3. Display all contacts")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            # Add a contact
            name = input("Enter the contact name: ")
            phone_number = input("Enter the phone number: ")
            phonebook[name] = phone_number
            print(f"Contact {name} added.")

        elif choice == '2':
            # Search for a contact
            name = input("Enter the contact name to search: ")
            if name in phonebook:
                print(f"{name}'s phone number is {phonebook[name]}.")
            else:
                print(f"Contact {name} not found.")

        elif choice == '3':
            # Display all contacts
            if phonebook:
                print("\nPhonebook Contacts:")
                for name, phone_number in phonebook.items():
                    print(f"{name}: {phone_number}")
            else:
                print("The phonebook is empty.")

        elif choice == '4':
            # Exit the program
            print("Exiting the phonebook.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()

