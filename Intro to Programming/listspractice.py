names = []
new_names = ""
while new_names != "End":
    new_names = input("Type the name of a friend (type end when finished): ").capitalize()
    if new_names != "End":
        names.append(new_names)
        
print("Your friends are: ")
for name in names:
    print(f"{name}")
