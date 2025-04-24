# There are times where we want to return different things from a function based on some condition. 
# To practice this idea, imagine that we want to check if someone is an adult. We might check their 
# age and return different things depending on how old they are!

ADULT_AGE = 18  # Define the age at which a person is considered an adult

def is_adult(age):
    return age >= ADULT_AGE  # Return True if age is greater than or equal to ADULT_AGE, otherwise False

def main():
    user_input = input("How old is this person?: ")
    try:
        age = int(user_input)  # Convert input to an integer
        result = is_adult(age)  # Call the function to check if the person is an adult
        print(result)  # Print the result (True or False)
    except ValueError:
        print("Please enter a valid integer.")  # Handle invalid input

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()