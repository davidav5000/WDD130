#Number Question
pos_num =int(input("Please input a positive number: "))
while pos_num <= 0:
    print("Sorry that is a negative number. Please try again.")
    pos_num =int(input("\nPlease input a positive number: "))
print(f"The number is: {pos_num}")
#Candy Question
candy =input("May I have a peice of candy? ").lower()
while candy == "no":
        candy =input("\nMay I have a peice of candy? ").lower()
if candy == "yes":
     print("\nThank you!")