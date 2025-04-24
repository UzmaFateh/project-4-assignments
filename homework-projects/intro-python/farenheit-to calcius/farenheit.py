# Write a program which prompts the user for a temperature in Fahrenheit 
# (this can be a number with decimal places!) and outputs 
# the temperature converted to Celsius.

def main():
    # Prompt the user for a temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Output the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# Run the program
if __name__ == "__main__":
    main()