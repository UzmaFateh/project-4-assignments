# Write a program which asks the user what their favorite animal is, and then always responds 
# with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted 
# animal, of course).

def main():
    # Prompt the user for their favorite animal
    favorite_animal = input("What's your favorite animal? ")
    
    # Respond with the favorite animal
    print(f"My favorite animal is also {favorite_animal}!")

# Run the program
if __name__ == "__main__":
    main()





