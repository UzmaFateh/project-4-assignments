# Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and continuing 
# as long as the terms are less than 10,000 (you should store this value as a constant!). Thus, your program 
# should produce the following sample run:

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765


def main():
    # Define the maximum value for the Fibonacci sequence
    MAX_VALUE = 10000

    # Initialize the first two terms of the Fibonacci sequence
    fib_0 = 0
    fib_1 = 1

    # Print the first term
    print(fib_0, end=' ')

    # Loop to generate Fibonacci terms
    while fib_1 < MAX_VALUE:
        print(fib_1, end=' ')
        # Calculate the next term
        next_fib = fib_0 + fib_1
        # Update the previous two terms
        fib_0 = fib_1
        fib_1 = next_fib

# Run the program
if __name__ == "__main__":
    main()