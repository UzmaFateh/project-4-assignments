# Simulate rolling two dice, three times. Prints the results of each die roll. 
# This program is used to show how variable scope works.

import random

def roll_two_dice():
    """Simulates rolling two dice and prints the results."""
    for _ in range(3):  # Roll the dice three times
        die1 = random.randint(1, 6)  # Roll the first die
        die2 = random.randint(1, 6)  # Roll the second die
        print(f"Roll: Die 1 = {die1}, Die 2 = {die2}")
        print(f"The sum of these die rolls is {die1 + die2}")

# Run the simulation
if __name__ == "__main__":
    roll_two_dice()