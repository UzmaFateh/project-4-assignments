# Fill out the function get_last_element(lst) which takes in a list lst as a parameter 
# and prints the last element in the list. The list is guaranteed to be non-empty, 
# but there are no guarantees on its length.

def get_last_element(lst):
    """Prints the last element of the list."""
    print("The last element is:", lst[-1])  # Access and print the last element

def main():
    # Prompt the user to input the list elements
    user_list = []
    num_elements = int(input("How many elements do you want to add to the list? "))

    for _ in range(num_elements):
        element = input("Enter an element: ")
        user_list.append(element)  # Add the element to the list

    # Call the function to get the last element
    get_last_element(user_list)

# Run the program
if __name__ == "__main__":
    main()