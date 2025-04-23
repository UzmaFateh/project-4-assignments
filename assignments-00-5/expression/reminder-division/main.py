# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by
#  the second and also the remainder of the division.

def main():
    # Prompt the user for the first number
    numerator = int(input("Please enter an integer to be divided: "))
    
    # Prompt the user for the second number
    denominator = int(input("Please enter an integer to divide by: "))
    
    # Perform the division and calculate the remainder
    result = numerator // denominator  # Integer division
    remainder = numerator % denominator  # Remainder
    
    # Output the result
    print(f"The result of this division is {result} with a remainder of {remainder}")

# Run the program
if __name__ == "__main__":
    main()

