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
bank = ["david", "nephi", "jacob", "moroni", "alma", "helaman", "ammon", "lehi", "sam", "zoram", "liahona", "zion"]
word = random.choice(bank)
word_count = range(len(word))
print("Welcome to the Wordle game!\n")
print("Your hint is:", end=" ")
for i, letter in enumerate(word):
    print("_", end="")
guess_number = 0
guess = input("\nWhat is your guess? ").lower()
guess_number += 1
while guess != word:
    if len(guess) != len(word):
        print("Sorry, The guess must have the same number of letters as the secret word.")
    else:
        correct_letters = []
        for i, letter in enumerate(guess):
            if letter == word[i]:
                #Capitalizes the first letter of the word
                if i == 0:
                    correct_letters.append(letter.upper())
                else:
                    correct_letters.append(letter.lower())
            elif letter in word:
                correct_letters.append(letter.lower())
            else:
                correct_letters.append("_")
        print(" ".join(correct_letters))
    guess = input("What is your guess? ").lower()
    guess_number += 1
if guess == word:
    print("\nCongratulations! You guessed it:", word.capitalize())
    print(f"\nIt took you {guess_number} guesses!")
