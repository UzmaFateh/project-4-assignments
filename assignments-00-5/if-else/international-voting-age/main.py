# Write a program which asks a user for their age and lets them know if they can or can't vote in the 
# following three fictional countries.
# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, 
# Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, 
# or Mayengua.

# PETURKSBOUIPO_AGE : int = 16
# STANLAU_AGE : int = 25
# MAYENGUA_AGE : int = 48

# def main():
#     # Get the user's age
#     user_age = int(input("How old are you? "))

#     # Check if the user can vote in Peturksbouipo
#     if user_age >= PETURKSBOUIPO_AGE:
#         print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
#     else:
#         print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    
#     # Check if the user can vote in Stanlau
#     if user_age >= STANLAU_AGE:
#         print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
#     else:
#         print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    
#     # Check if user can vote in Mayengua
#     if user_age >= MAYENGUA_AGE:
#         print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
#     else:
#         print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()

def main():
    # Ask the user for their age
    age_input = input("How old are you? ")
    
    try:
        # Convert input to an integer
        age = int(age_input)

        # Check voting eligibility for Peturksbouipo
        if age >= 16:
            print("You can vote in Peturksbouipo where the voting age is 16.")
        else:
            print("You cannot vote in Peturksbouipo where the voting age is 16.")

        # Check voting eligibility for Stanlau
        if age >= 25:
            print("You can vote in Stanlau where the voting age is 25.")
        else:
            print("You cannot vote in Stanlau where the voting age is 25.")

        # Check voting eligibility for Mayengua
        if age >= 48:
            print("You can vote in Mayengua where the voting age is 48.")
        else:
            print("You cannot vote in Mayengua where the voting age is 48.")

    except ValueError:
        print("Please enter a valid number for your age.")

# Run the program
if __name__ == "__main__":
    main()