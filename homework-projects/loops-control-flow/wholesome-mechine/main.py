# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing '
# 'anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain 
# times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be 
# able to help!

def main():
    # Define the affirmation
    affirmation = "I am worthy of best."
   

    while True:
        # Prompt the user to type the affirmation
        user_input = input("Please type the following affirmation: ")

        # Check if the input matches the affirmation
        if user_input == affirmation:
            print("That's 100% right! :)")
            break  # Exit the loop if the affirmation is correct
        else:
            print("Hmmm! That was not the affirmation.")

# Run the program
if __name__ == "__main__":
    main()