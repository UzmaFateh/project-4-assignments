def check_height(height):
    # Minimum height requirement
    minimum_height = 50
    
    if height >= minimum_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def main():
    while True:
        # Ask the user for their height
        user_input = input("How tall are you ,put the value in inches? (Press Enter to quit) ")
        
        # Check if the user wants to quit
        if user_input == "":
            print("Thank you for participating!")
            break
        
        try:
            # Convert input to an integer
            height = int(user_input)
            # Check if the height meets the requirement
            check_height(height)
        except ValueError:
            print("Please enter a valid number for your height.")

# Run the program
if __name__ == "__main__":
    main()