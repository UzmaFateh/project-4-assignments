# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

def main():
    # Given age of Anton
    anton_age = 21
    
    # Calculate ages based on the relationships
    beth_age = anton_age + 6
    chen_age = beth_age + 20
    drew_age = chen_age + anton_age
    ethan_age = chen_age
    
    # Print the names and ages
    print(f"Anton is {anton_age} years old.")
    print(f"Beth is {beth_age} years old.")
    print(f"Chen is {chen_age} years old.")
    print(f"Drew is {drew_age} years old.")
    print(f"Ethan is {ethan_age} years old.")

# Run the program
if __name__ == "__main__":
    main()