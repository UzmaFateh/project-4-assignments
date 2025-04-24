# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a 
# parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 
#                                                                                in stock)

# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

# Here's two sample runs of the program (user input in bold italics):

# Enter a fruit: pear

# This fruit is in stock! Here is how many:

# 1000

# Enter a fruit: lychee

# This fruit is not in stock.


# Sample inventory for demonstration purposes
inventory = {
    "apple": 50,
    "banana": 30,
    "pear": 1000,
    "orange": 0,
    "grape": 200
}

def num_in_stock(fruit):
    """ Returns the number of the specified fruit in stock. """
    return inventory.get(fruit, 0)  # Return the count of the fruit or 0 if not found

def main():
    fruit = input("Enter a fruit: ")  # Prompt for a fruit
    stock_count = num_in_stock(fruit)  # Get the number of that fruit in stock

    if stock_count > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock_count)  # Print the number in stock
    else:
        print("This fruit is not in stock.")  # Print if the fruit is not in stock

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()