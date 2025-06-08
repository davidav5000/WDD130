import random
number =random.randint(1,100)
print("What is the magic number? ")
guess =int(input("What is your guess? "))
while guess != number:
    if guess > number:
        print("Lower...")
        guess =int(input("What is your guess? "))
    elif guess < number:
        print("Higher...")
        guess =int(input("What is your guess? "))
else:
    print("You guessed it!")
