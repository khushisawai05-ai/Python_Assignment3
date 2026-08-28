# Create a simple menu-driven program to perform operations on a dictionary
items = {}

while True:
    print("\n1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. Search Item")
    print("5. Display Items")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        items[key] = value
        print("Item added successfully.")

    elif choice == 2:
        key = input("Enter key: ")

        if key in items:
            value = input("Enter new value: ")
            items[key] = value
            print("Item updated successfully.")
        else:
            print("Item not found.")

    elif choice == 3:
        key = input("Enter key: ")

        if key in items:
            del items[key]
            print("Item deleted successfully.")
        else:
            print("Item not found.")

    elif choice == 4:
        key = input("Enter key: ")

        if key in items:
            print("Value:", items[key])
        else:
            print("Item not found.")

    elif choice == 5:
        print("Items:", items)

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")