print("Welcome to the Shopping Cart Program!")
action = "0"
items = []
prices = []
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
        price =float(input(f"\nWhat is the price of '{new_item}'? "))
        prices.append(price)
        print(f"\n'{new_item}' has been added to the cart")
        

    elif action == "2":
        print(f"\nThe Contents of the Shopping Cart are:")
        for i in range(len(items)):
            print(f"{items[i]} - ${prices[i]:.2f}")

    elif action == "3":
        print("\nThe Contents of the Shopping Cart are:")
        for i in range(len(items)):
            print(f"{i+1}. {items[i]} - ${prices[i]}")
        remove_index = int(input("\nWhich item number would you like to remove? ")) - 1
        if 0 <= remove_index < len(items):
            removed_item = items.pop(remove_index)
            removed_price = prices.pop(remove_index)
            print(f"'{removed_item}' has been removed from the cart.")
        else:
            print("Invalid item number.")
        
    elif action =="4":
        sum = 0
        for i in range(len(prices)):
            sum = sum + prices[i]
        print(f"\nThe total price of the items in the shopping cart is ${sum:.2f}")

    elif action == "5":
        print("\nThank you. Goodbye")
        break

