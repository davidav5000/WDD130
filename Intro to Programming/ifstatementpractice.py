firstnum =input("Enter a number: ")
secnum =input("Enter a second number: ")
firstnum_input = int(firstnum)
secnum_input = int(secnum)
if firstnum_input > secnum_input:
    print(f"\n{firstnum_input} is greater than {secnum_input}.\n{firstnum_input} and {secnum_input} are not equal\n{secnum_input} is not greater than than {firstnum_input}")
elif firstnum_input < secnum_input:
    print(f"\n{secnum_input} is greater than {firstnum_input}.\n{secnum_input} and {firstnum_input} are not equal\n{firstnum_input} is not greater than {secnum_input}")
elif firstnum_input == secnum_input:
    print(f"\nBoth {firstnum_input} and {secnum_input} are equal.")

#Animal Preference
animal = input("\nWhat is your favorite animal? ").title()
armadillo = "Armadillo"
if animal == armadillo:
    print(f"\n{armadillo}s are my favorite animal too!")
elif animal != armadillo:
    print(f"\nThe {animal} is not my favorite.")
