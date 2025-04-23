# Write a program that asks a user to enter a number. Your program will then double that number and 
# print out the result. It will repeat that process until the value is 100 or greater.

def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Loop to double the number until it is 100 or greater
    while curr_value < 100:
        curr_value *= 2  # Double the current value
        print(curr_value, end=' ')  # Print the current value followed by a space
   
# Run the program
if __name__ == "__main__":
    main()