print("Welcome to the Shopping Cart Program!")
action = "0"
while True:
    print("Please select one of following:")
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute Total")
    print("5. Quit")
    action =input("Please Enter an Action: ")
    if action == "1":
        items = []
        new_item =input("What item would you like to add:")
        items.append(new_item)
    elif action == "5":
        print("Thank you. Goodbye")
        break
