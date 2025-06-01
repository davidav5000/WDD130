age =input("What is the age of the first rider? ")
height =input("What is the height of the first rider? ")
secondrider =input("Is there a second rider (yes/no)? ").lower()
age_input = int(age)
height_input = int(height)
if height_input < 36:
    print("Sorry, you may not ride.")
else:
    if secondrider == "yes":
        agesecond =input("What is the age of the second rider? ")
        agesecond_input = int(agesecond)
        heightsecond =input("What is the height of the second rider? ")
        heightsecond_input = int(heightsecond)
        if heightsecond_input < 36:
                print("Sorry you may not ride.")
        else:
            if agesecond_input < 18 and age_input >= 18 or agesecond_input >= 18 and age_input < 18:

            if height_input >= 62 and heightsecond_input < 62 or heightsecond_input > 62 and height_input < 62


            print("Sorry, you may not ride")
    elif secondrider =="no":
        if age_input > 18 and height_input > 62:
            print("Welcome to the ride. Please be safe and have fun")
        else:
            print("Sorry, you may not ride")