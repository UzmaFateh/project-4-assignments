# Fill out the get_name() function to return your name as a string! We've written a main() function for 
# you which calls your function to retrieve your name and then prints it in a greeting.


def get_name():
    return "Mariyam"  # Return the name as a string

def main():
    name = get_name()  # Call the get_name function to retrieve the name
    print(f"Howdy {name} ! 🤠")  # Print the greeting with the name

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()