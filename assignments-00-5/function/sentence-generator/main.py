# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an 
# integer part_of_speech as parameters and, depending on the part of speech, place the word into one of 
# three sentence templates (or one from your imagination!):

# If part_of_speech is 0, we will assume the word is a noun and use the template: "I am excited to add 
# this ____ to my vast collection of them!"

# If part_of_speech is 1, we will assume the word is a verb use the template: "It's so nice outside today 
# it makes me want to ____!"

# If part_of_speech is 2, we will assume the word is an adjective and use the template: "Looking out my 
# window, the sky is big and ____!" make_sentence(word, part_of_speech) should not return anything, just 
# print the correct sentence with the word filled in the blank.


def make_sentence(word, part_of_speech):
    if part_of_speech == 0:  # Noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # Verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # Adjective
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech. Please enter 0, 1, or 2.")

def main():
    word = input("Please type a noun, verb, or adjective: ")  # Prompt for a word
    user_input = input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: ")
    
    try:
        part_of_speech = int(user_input)  # Convert input to an integer
        make_sentence(word, part_of_speech)  # Call the function to make a sentence
    except ValueError:
        print("Please enter a valid integer (0, 1, or 2).")  # Handle invalid input

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()