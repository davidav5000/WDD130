# print ("Welcome to the Word game!\n")
# key = "David"
# guess = input("What is your guess? ").title()
# count = 0
# while guess != key:
#     print("Incorrect guess, try again!")
#     guess = input("What is your guess? ").title()
#     count += 1
# if guess == key:
#     print("\nCongratulations, you guessed the word! It was David.")
#     print(f"\nYou guessed the word in {count} tries!")

# word = "commitment"
# fav_letter = input("What is your favorite letter? ")
# for letter in word:
#     if letter.lower() == fav_letter.lower():
#         print("_", end="")
#     else:
#         print(letter.lower(), end="")
# print()

# quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
# loop = "yes"
# while loop == "yes":
#     number = int(input("Number? "))
#     for i, letter in enumerate(quote):
#         if i % number == 0:
#             print(letter.upper(), end="")
#         else:
#             print(letter.lower(), end="")
#     loop = input("\nDo you want to continue? (yes/no) ").lower()
# print("\nThank you for using the program!")

import random
print("Welcome to the Wordle game!\n")
bank = ["david","dan"]
word = random.choice(bank)
word_count = range(len(word))
print("Your hint is:", end=" ")
for i, letter in enumerate(word):
    print("_", end="")
guess = input("\nWhat is your guess? ")  
guess_input = range(len(guess))
if len(guess) != len(word):
    print("Your guess is not the same length as the word.")
else:
    print("Your guess is:", end=" ")