usergrade = input("Enter your grade percentage: ")
usergrade = float(usergrade)
if usergrade >= 97:
    print("You got an A.")
elif usergrade >= 93:
    print("You got an A-!")
elif usergrade >= 88:
    print("You got a B+!")
elif usergrade >= 87:
    print("You got a B!")
elif usergrade >= 83:
    print("You got a B-!")
elif usergrade >= 78:
    print("You got a C+!")
elif usergrade >= 76:
    print("You got a C!")
elif usergrade >= 73:
    print("You got a C-!")
elif usergrade >= 68:
    print("You got a D+!")
elif usergrade >= 67:
    print("You got a D!")
elif usergrade >= 63:
    print("You got a D-!")
elif usergrade >= 60:
    print("You got an F!")
if usergrade >= 70:
    print("You passed! Congratulations!")
else:
    print("You failed. Try harder next time!")
