# Write a function that takes a list of numbers and returns the sum of those numbers.


def sum_of_numbers(numbers):
    """Returns the sum of a list of numbers."""
    total = 0  # Initialize the total sum to 0
    for number in numbers:
        total += number  # Add each number to the total
    return total  # Return the final sum

# Example usage
if __name__ == "__main__":
    # Sample list of numbers
    num_list = [1, 2, 3, 4, 5,6]
    result = sum_of_numbers(num_list)
    print(f"The sum of the numbers is: {result}")