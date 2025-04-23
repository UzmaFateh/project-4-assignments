# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to 
# call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

def subtract_seven(num):
    """Subtracts 7 from the given number."""
    return num - 7  # Return the result of subtracting 7 from num

def main():
    user_input = input("Enter a number: ")  # Prompt for a number
    try:
        number = int(user_input)  # Convert input to an integer
        result = subtract_seven(number)  # Call the helper function
        print(f"The result after subtracting 7 is: {result}")  # Print the result
    except ValueError:
        print("Please enter a valid integer.")  # Handle invalid input

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()