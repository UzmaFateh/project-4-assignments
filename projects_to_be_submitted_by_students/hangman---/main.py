import random
import time

categories = {
    'Animals': ['Dog', 'tiger', 'elephent', 'cat', 'kangaroo'],
    'Fruits': ['apple', 'orange', 'banana', 'cherry'],
    'Countries': ['pakistan', 'palestine', 'china'],
    'Cities': ['lahore', 'islamabad', 'karachi']
}

def give_hint(word):
    return f"The word starts with: {word[0]}"

def get_valid_input(guessed_letters, incorrect_guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
        elif guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter!")
        else:
            return guess

def set_difficulty():
    while True:
        difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
        if difficulty == 'easy':
            return 8
        elif difficulty == 'medium':
            return 6
        elif difficulty == 'hard':
            return 4
        else:
            print("Invalid choice. Please choose again.")

def hangman_game():
    print("Choose a category:")
    for category in categories:
        print(category)
    category = input("Enter category: ").capitalize()

    word = random.choice(categories.get(category, []))
    if not word:
        print(f"No words found for category {category}. Try again.")
        return False, 0

    word = word.lower()
    word_length = len(word)
    guesses_left = set_difficulty()
    guessed_letters = []
    incorrect_guesses = []
    display = ['_'] * word_length

    start_time = time.time()
    time_limit = 60
    hint_used = False

    if not hint_used:
        if input("Want a hint? (yes/no): ").lower() == "yes":
            print(give_hint(word))
            hint_used = True

    while guesses_left > 0 and '_' in display:
        print(f"\nWord: {' '.join(display)}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Guesses left: {guesses_left}")
        print(f"Time left: {max(0, time_limit - int(time.time() - start_time))} seconds")

        if time.time() - start_time > time_limit:
            print("Time's up! You lose.")
            return False, guesses_left

        guess = get_valid_input(guessed_letters, incorrect_guesses)

        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            guessed_letters.append(guess)
            display = [guess if word[i] == guess else display[i] for i in range(word_length)]
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            incorrect_guesses.append(guess)
            guesses_left -= 1

    if '_' not in display:
        print(f"Congratulations! You've guessed the word: {word}")
        return True, guesses_left
    else:
        print(f"Game Over! The word was: {word}")
        return False, guesses_left

def play_hangman():
    total_games = 0
    games_won = 0
    high_score = float('inf')

    while True:
        print("\nStarting a new game...")
        game_won, guesses_left = hangman_game()

        total_games += 1
        if game_won:
            games_won += 1
            high_score = min(high_score, guesses_left)

        print(f"\nTotal Games Played: {total_games}")
        print(f"Games Won: {games_won}")
        if games_won > 0:
            print(f"High Score (Fewest guesses left): {high_score}")
        else:
            print("High Score: N/A (no wins yet)")

        if input("\nDo you want to play again? (yes/no): ").lower() != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_hangman()

    