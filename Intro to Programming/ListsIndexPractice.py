items = []
new_item = ""
while new_item != "Quit":
    new_item = input("Please enter the items of the shopping list (type: quit to finish): ").capitalize()
    items.append(new_item)
    if new_item == "Quit":
        break
print("The Shopping list is: ")
for item in items:
    print(item)
print("")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")
print("")
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

items[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")