# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that
#  outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.


import math

def calculate_hypotenuse(ab, ac):
    """Calculates the length of the hypotenuse using the Pythagorean theorem."""
    return math.sqrt(ab**2 + ac**2)

def main():
    # Prompt the user for the lengths of the two sides
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))
    
    # Calculate the hypotenuse
    bc = calculate_hypotenuse(ab, ac)
    
    # Output the result
    print(f"The length of BC (the hypotenuse) is: {bc}")

# Run the program
if __name__ == "__main__":
    main()