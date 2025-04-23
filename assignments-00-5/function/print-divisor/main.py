# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors 
# (all the numbers from 1 to num inclusive that num can be cleanly divided by 
#  (there is no remainder to the division). Don't forget to call your function in main()!

def print_divisors(num):
    print(f"Here are the divisors of {num}:")
    for i in range(1, num + 1):  # Loop from 1 to num inclusive
        if num % i == 0:  # Check if i is a divisor of num
            print(i, end=' ')  # Print the divisor
    print()  # Print a newline at the end

def main():
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)  # Convert input to an integer
        print_divisors(number)  # Call the function to print divisors
    except ValueError:
        print("Please enter a valid integer.")  # Handle invalid input

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()