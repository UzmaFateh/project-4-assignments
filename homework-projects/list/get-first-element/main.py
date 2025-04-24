# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and 
# prints the first element in the list. The list is guaranteed to be non-empty. We've written 
# some code for you which prompts the user to input the list one element at a time.

def get_first_element(lst):
    """Prints the first element of the list."""
    print("The first element is:", lst[0])  # Access and print the first element

def main():
    # Prompt the user to input the list elements
    user_list = []
    num_elements = int(input("How many elements do you want to add to the list? "))

    for _ in range(num_elements):
        element = input("Enter an element: ")
        user_list.append(element)  # Add the element to the list

    # Call the function to get the first element
    get_first_element(user_list)

# Run the program
if __name__ == "__main__":
    main()