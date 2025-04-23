# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high


import random

def main():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    guess = None

    print("I am thinking of a number between 0 and 99...")

    # Loop until the user guesses the correct number
    while guess != secret_number:
        # Prompt the user for a guess
        guess = int(input("Enter a guess: "))

        # Check if the guess is too high, too low, or correct
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congrats! The number was: {secret_number}")

# Run the program
if __name__ == "__main__":
    main()