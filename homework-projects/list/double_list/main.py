# Write a program that doubles each element in a list of numbers.

def double_numbers(numbers):
    """Doubles each element in the list of numbers."""
    for i in range(len(numbers)):
        numbers[i] *= 2  # Double the current element

# Example usage
if __name__ == "__main__":
    # Initial list of numbers
    numbers = [1, 2, 3, 4]
    print("Original list:", numbers)

    # Double each element in the list
    double_numbers(numbers)

    # Print the updated list
    print("Doubled list:", numbers)

