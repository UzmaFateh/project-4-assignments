# Ask the user for a number and print its square (the product of the number times itself).

def main():
    # Prompt the user for a number
    number = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    square = number * number
    
    # Print the result
    print(f"{number} squared is {square}")

# Run the program
if __name__ == "__main__":
    main()
    