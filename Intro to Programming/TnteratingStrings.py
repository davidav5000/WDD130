# word = "commitment"
# fav_letter = input("What is your favorite letter? ")
# for letter in word:
#     if letter.lower() == fav_letter.lower():
#         print("_"(), end="")
#     else:
#         print(letter.lower(), end="")
# print()

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
loop = "yes"
while loop == "yes":
    number = int(input("Number? "))
    for i, letter in enumerate(quote):
        if i % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    loop = input("\nDo you want to continue? (yes/no) ").lower()
print("\nThank you for using the program!")

