# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. 
import random


DONE_LIKELIHOOD = 0.3  # 30% chance to return True
def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return  # Exit the function if done() returns True
        print(i, end=' ')
    # If we reach here, we counted to 10 without stopping

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")

# Run the main function
if __name__ == "__main__":
    main()