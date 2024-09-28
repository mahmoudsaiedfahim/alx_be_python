'''This script implements a simple interface for managing a shopping list. 
This task focuses on using lists to store and manipulate data dynamically.'''

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item_name = input("Please enter item name to add: ")
            shopping_list.append(item_name)
        elif choice == '2':
            # Prompt for and remove an item
            item_name = input("Please enter item name to remove: ")
            if item_name in shopping_list:
                shopping_list.remove(item_name)
            else:
                print("Item name is not exist in shopping list!")
        elif choice == '3':
            # Display the shopping list
            if len(shopping_list)==0:
                print("No items in shopping list!")
            else:
                print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
