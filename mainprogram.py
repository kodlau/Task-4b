# File name: mainprogram.py
# Author: Lauri Kodisoja
# Description: A file that runs the whole program.


from displaymenu import display_menu
from functions import search_element, add_element, remove_element, sort_list, list_elements, count_elements


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