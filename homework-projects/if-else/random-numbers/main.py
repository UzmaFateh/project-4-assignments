import random

def generate_random_numbers():
    # Generate 10 random numbers in the range 1 to 100
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    return random_numbers

def main():
    # Get random numbers
    numbers = generate_random_numbers()
    # Print the random numbers
    print(" ".join(map(str, numbers)))

# Run the program
if __name__ == "__main__":
    main()