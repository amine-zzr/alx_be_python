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
            shopping_list.append(input("Enter the item to add: "))
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Item name: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"'{item}' was not on the list")
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("your list is empty")
            else:
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
