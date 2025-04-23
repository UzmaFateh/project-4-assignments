# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

# Function to roll two dice
def roll_dice():
    die1 = random.randint(1, 6)  # Roll first die
    die2 = random.randint(1, 6)  # Roll second die
    total = die1 + die2          # Calculate total
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")

# Simulate rolling the dice
roll_dice()