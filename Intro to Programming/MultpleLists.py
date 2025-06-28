import math
names = []
balances = []
name = ""
balance = ""
while name != "quit":
    print()
    print("Enter the names and balences of bank accounts")
    name = input("What is the name of the account: ").lower()
    if name != "quit":
        names.append(name)
        balance = float(input("What is the balance: "))
        if balance != "quit":
            balances.append(balance)
print("Account Information:")
for i in range(len(names)):
        print(f"{names[i]} - ${balances[i]:.2f} ")
sum = 0
for i in range(len(balances)):
     sum = sum + balances[i]
print(f"\nTotal: ${sum:.2f}")
avarage = sum / len(balances)
print(f"Avarage: ${avarage:.2f}")