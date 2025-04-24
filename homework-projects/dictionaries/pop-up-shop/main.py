# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, 
# you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were 
# available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they 
# want to buy, and then prints out the total combined cost of all of the fruits.

def main():
    # Dictionary of fruits and their prices
    fruit_prices = {
        "apple": 1.50,
        "banana": 2.00,
        "orange": 7.00,
        "jackfruit": 3.00,
        "kiwi": 2.00,
        "dragonfruit": 8.00,
        "mango": 7.50
    }

    total_cost = 0.0

    # Loop through the dictionary and prompt the user for quantities
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price

    # Print the total cost
    print(f"\nYour total is ${total_cost:.2f}")

# Run the program
if __name__ == "__main__":
    main()