# Fill out the function shorten(lst) which removes elements from the end of lst, 
# which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 
# If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() 
# function for you which gets a list and passes it into your function once you run the program. 
# For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to 
# test your program.



def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)


MAX_LENGTH : int = 3


def get_lst_element():
    """
    Prompts the user to enter one element of the list and returns the resulting list.
    """
    lst = []
    element = input("Please enter an element of the list or press enter to stop. ")
    while element != "":
        lst.append(element)
        element = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst_element()
    shorten(lst)


if __name__ == '__main__':
    main()