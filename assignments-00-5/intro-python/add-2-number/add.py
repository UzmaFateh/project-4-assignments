# Write a Python program that takes two integer inputs from the user and calculates their sum.


def main():
    # Prompt the user for the first number
    first_number = int(input("Please enter the first number: "))
    
    # Prompt the user for the second number
    second_number = int(input("Please enter the second number: "))
    
    # Calculate the sum of the two numbers
    total_sum = first_number + second_number
    
    # Print the total sum with an appropriate message
    print(f"The total sum of {first_number} and {second_number} is: {total_sum}")

# Run the program
if __name__ == "__main__":
    main()