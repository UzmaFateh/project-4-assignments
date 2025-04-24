# Write a program which prompts the user for an adjective,
#  then a noun, then a verb, and then prints a fun sentence with those words!


def main():
    # Predefined sentence start
    SENTENCE_START = "I learned to program and used Python to make my"

    # Prompt the user for input
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Construct the final sentence
    final_sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"

    # Print the result
    print(final_sentence)

# Run the program
if __name__ == "__main__":
    main()