def double(num):
    return num * 2

def main():
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)  # Convert input to a float
        result = double(number)  # Call the double function
        print("Double that is", result)  # Print the result
    except ValueError:
        print("Please enter a valid number.")  # Handle invalid input

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()