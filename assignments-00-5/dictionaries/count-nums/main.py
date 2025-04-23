# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of 
# the information.



# Initialize an empty dictionary to store counts
number_counts = {}

# Loop to get user input
while True:
    user_input = input("Enter a number (or type 'done' to finish): ")
    
    if user_input.lower() == 'done':
        break
    
    try:
        # Convert input to an integer
        number = int(user_input)
        
        # Update the count in the dictionary
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1
            
    except ValueError:
        print("Please enter a valid number.")

# Print the frequency of each number
for number, count in number_counts.items():
    print(f"{number} appears {count} times.")