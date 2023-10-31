# File name: functions.py
# Author: Lauri Kodisoja
# Description: A file that has all the functions used by the program.


from list import my_list

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