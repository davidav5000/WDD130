print ("Welcome to the Word game!\n")
key = "David"
guess = input("What is your guess? ").title()
count = 0
while guess != key:
    print("Incorrect guess, try again!")
    guess = input("What is your guess? ").title()
    count += 1
if guess == key:
    print("\nCongratulations, you guessed the word! It was David.")
    print(f"\nYou guessed the word in {count} tries!")