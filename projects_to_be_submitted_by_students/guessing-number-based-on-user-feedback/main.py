# This code shows a number guessing game where the computer 
# tries to guess a number that the user is thinking of, based on the user's feedback.

import random
import time

def guess_the_number_user():
    print("Welcome to the Guess the Number Game!")
    print("Think of a number and I will try to guess it.")

    try:
        low = int(input("Enter the lower limit of your number range: "))
        high = int(input("Enter the upper limit of your number range: "))
    except ValueError:
        print("Invalid input! Please enter valid integers.")
        return

    if low >= high:
        print("The lower limit should be less than the upper limit. Try again.")
        return

    print(f"Great! I'm going to guess a number between {low} and {high}.")
    time.sleep(1)

    attempts = 0
    hint = ""

    while True:
        attempts += 1
        guess = (low + high) // 2

        print(f"Attempt {attempts}: My guess is {guess} {hint}")

        feedback = input("Is my guess too high, too low, or correct? (h/l/c): ").lower()

        if feedback == 'c':
            print(f"Yay! I guessed the correct number {guess} in {attempts} attempts. 🎉")
            break
        elif feedback == 'h':
            high = guess - 1
            hint = "🔼"
        elif feedback == 'l':
            low = guess + 1
            hint = "🔽"
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
            attempts -= 1


        if attempts % 5 == 0 and attempts != 0:
            print("Tip: You're getting close! Keep going!")

guess_the_number_user()