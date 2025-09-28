# shopping_list_manager.py

def display_menu():
    print("\n=== Shopping List Manager ===")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []  # start with an empty list
    
    while True:
        display_menu()
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":  # Add item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"{item} has been added to the list.")
            else:
                print("Item name cannot be empty.")
        
        elif choice == "2":  # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list.")
            else:
                print(f"{item} not found in the shopping list.")
        
        elif choice == "3":
            if shopping_list:
                print("\nCurrent Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is empty.")
        
        elif choice == "4":
            print("Exiting Shopping List Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
