# Write a program that continually reads in mass from the user and then outputs 
# the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, 
# m stands for mass, and C is the speed of light:

# E = m * c**2

def calculate_energy(mass):
    """Calculates energy using Einstein's mass-energy equivalence formula."""
    C = 299792458  # Speed of light in m/s
    energy = mass * (C ** 2)  # E = m * c^2
    return energy

def main():
    while True:
        # Prompt the user for mass input
        user_input = input("Enter kilos of mass (or press Enter to quit): ")
        
        # Check if the user wants to exit
        if user_input == "":
            print("Exiting the program.")
            break
        
        try:
            mass = float(user_input)  # Convert input to float
            print("\ne = m * C^2...")
            print(f"m = {mass} kg")
            print(f"C = 299792458 m/s")
            
            # Calculate energy
            energy = calculate_energy(mass)
            print(f"{energy} joules of energy!")
        
        except ValueError:
            print("Please enter a valid number for mass.")

# Run the program
if __name__ == "__main__":
    main()