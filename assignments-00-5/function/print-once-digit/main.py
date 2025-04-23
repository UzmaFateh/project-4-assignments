# Write a function called print_ones_digit , which takes as a parameter an integer num and prints 
# its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function 
# from main()!

def print_ones_digit(num):
    ones_digit = num % 10  # Calculate the ones digit using the modulo operator
    print(f"The ones digit is {ones_digit}")  # Print the ones digit

def main():
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)  # Convert input to an integer
        print_ones_digit(number)  # Call the function to print the ones digit
    except ValueError:
        print("Please enter a valid integer.")  # Handle invalid input

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()