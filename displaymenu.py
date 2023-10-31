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
