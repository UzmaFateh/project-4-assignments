# Function to check if a year is a leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # It's a leap year
            else:
                return False  # Not a leap year
        else:
            return True  # It's a leap year
    else:
        return False  # Not a leap year

# Main program
def main():
    # Read year from user
    year = int(input("Enter a year: "))
    
    # Check if it's a leap year
    if is_leap_year(year):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Run the program
if __name__ == "__main__":
    main()