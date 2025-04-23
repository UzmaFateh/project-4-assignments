# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a 
# loop of some sort. Do no write twenty print statements

# The first even number is 0:


def main():
    # Initialize an empty list to store even numbers
    even_numbers = []

    # Loop to generate the first 20 even numbers
    for i in range(20):
        even_number = i * 2
        even_numbers.append(even_number)

    # Print the even numbers in a single line
    print(" ".join(map(str, even_numbers)))

# Run the program
if __name__ == "__main__":
    main()