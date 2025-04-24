# Write a program that prints out the calls for a spaceship that is about to launch. 
# Countdown from 10 to 1 and then output Liftoff!

def main():
    # Countdown from 10 to 1
    for i in range(10, 0, -1):
        print(i, end=' ')  # Print the countdown number followed by a space

    # Print Liftoff!
    print("Liftoff!")

# Run the program
if __name__ == "__main__":
    main()