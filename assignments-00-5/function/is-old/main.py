#  Checks to see if a value is odd. 
def main():
    for num in range(10, 24):  # Loop through numbers from 10 to 19
        if num % 2 == 0:
            print(f"{num} even", end=' ')  # Print even numbers
        else:
            print(f"{num} odd", end=' ')   # Print odd numbers
    print()  # Print a newline at the end

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()