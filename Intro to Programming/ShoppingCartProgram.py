print("Welcome to the Shopping Cart Program!")
action = "0"
items = []
while True:
    print("\nPlease select one of following:")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute Total")
    print("5. Quit")
    action =input("Please Enter an Action: ")

    if action == "1":
        new_item =input("\nWhat item would you like to add: ")
        items.append(new_item)

    elif action == "2":
        print(f"\nThe Contents of the Shopping Cart are:")
        for item in items:
            print(item)

    elif action == "5":
        print("Thank you. Goodbye")
        break

