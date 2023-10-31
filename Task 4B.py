# File name: Task 4B.py
# Author: Lauri Kodisoja
# Description: A program that demonstrates the use of functions on a list.

"""Defines a list with 30 elements"""
my_list = [1, 2.2, "Manu Chao", 4, "Clandestino", 
           "Radio Bemba", 7, "Machine Gun", 9.9, 10, 
           "Rainin' In Paradize", 12, 13, "Mr Bobby", 15, 
           "Me Gustas Tu", 17.7, 18, 19.9, 20.0, 
           21.1, 22, 23, 24.5, "Desaparecido",
           26, 27.0, "La Primavera", 29.9, 30]

"""Defines a function to search for an element and its index in the list"""
def search_element():

    element = input("Enter the element you want to search: ")
    try:
        element = int(element)
    except ValueError:
        try:
            element = float(element)
        except ValueError:
            pass
    if element in my_list:
        print("\n" + "Element found at index:", my_list.index(element))
        print()
    else:
        print("\n" + "Element not found in the list" + "\n")

"""Defines a function to add an element to the list"""
def add_element():

    element = input("Enter the element you want to add: ")
    my_list.append(element)
    print("\n" + "Element added to the list" + "\n")

"""Defines a function to remove an element from the list"""
def remove_element():

    element = input("Enter the element you want to remove: ")
    try:
        element = int(element)
    except ValueError:
        try:
            element = float(element)
        except ValueError:
            pass
    if element in my_list:
        my_list.remove(element)
        print("\n" + "Element removed from the list" + "\n")
    else:
        print("\n" + "Element not found in the list" + "\n")

"""Defines a function to sort the list in numerical order and alphabetical order"""
def sort_list():

    my_list.sort(key=lambda x: (isinstance(x, str), x))
    print("\n" + "List sorted in ascending order" + "\n")

"""Defines a function to list all the elements in the list"""
def list_elements():

    print("\n" + "Elements in the list:" + "\n")
    for element in my_list:
        print(element)
    print()

"""Defines a function to count how many elements there are in the list"""
def count_elements():

    count = len(my_list)
    print("\n" + "Number of elements in the list:", count)
    print()

"""Defines a function to display the menu and get user input"""
def display_menu():

    print("Press number to select:" + "\n" )
    print("1. Stop")
    print("2. Search")
    print("3. Add")
    print("4. Remove")
    print("5. Sort")
    print("6. List all the elements")
    print("7. Count how many elements there are in the list")

    while True:
        try:
            choice = int(input("\n" + "Enter your choice: "))
            print()
            return choice
        except ValueError:
            print("\n" + "Invalid choice, please enter a number." + "\n")

"""Defines the main function to run the program"""
def main():

    choice = display_menu()
    
    while choice != 1:
        
        if choice == 2:
            search_element()
        
        elif choice == 3:
            add_element()
        
        elif choice == 4:
            remove_element()
        
        elif choice == 5:
            sort_list()
        
        elif choice == 6:
            list_elements()
        
        elif choice == 7:
            count_elements()
        
        else:
            print("Invalid choice")
        
        choice = display_menu()

    print("Shutting down the program")

"""Call the main function to run the program"""
main()