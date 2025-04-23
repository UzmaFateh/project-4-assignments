import random
import time

def get_number(level):
    if level == "easy":
        return random.randint(1, 10)
    elif level == "medium":
        return random.randint(1, 50)
    else:
        return random.randint(1, 100)

def get_hint(number):
    hints = []
    if number % 2 == 0:
        hints.append("The number is even.")
    else:
        hints.append("The number is odd.")
    if number % 5 == 0:
        hints.append("It is a multiple of 5.")
    if number > 50:
        hints.append("It is greater than 50.")
    elif number < 50:
        hints.append("It is less than 50.")
    return random.choice(hints)

def guess_game():
    print("Welcome to the Guess the Number Game!")
    print("Choose a difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    choice = input("Enter your choice (easy/medium/hard): ").lower()
    number = get_number(choice)
    lives = 7
    attempts = 0
    hint_given = False

    start_time = time.time()

    while lives > 0:
        try:
            guess = int(input(f"\nGuess the number (Lives left: {lives}): "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                end_time = time.time()
                print(f"\nCongratulations! You guessed the number {number} correctly.")
                print(f"Total Attempts: {attempts}")
                print(f"Time Taken: {round(end_time - start_time, 2)} seconds")
                break

            lives -= 1

            if lives == 4 and not hint_given:
                want_hint = input("Do you want a hint? (y/n): ").lower()
                if want_hint == 'y':
                    print("Hint:", get_hint(number))
                    hint_given = True

        except ValueError:
            print("Invalid input! Please enter a number.")

    if lives == 0:
        print(f"\nGame Over! The correct number was {number}.")

    again = input("\nDo you want to play again? (y/n): ").lower()
    if again == 'y':
        guess_game()
    else:
        print("Thanks for playing! Goodbye.")
guess_game()