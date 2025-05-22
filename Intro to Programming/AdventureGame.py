#adventure game start
print ("Welcome to the Choose your own Adventure Game! (Space Edition)")
print ("\nYou are a space explorer captain on a mission to find a new planet for humanity. \nEarth has become uninhabitable, and your task is to find a suitable replacement.")
planet = input("\nYou have two options for planets to explore: Planet H01DE55R or Planet C01DB1ZD. Which one do you choose? ").upper()
if planet == "H01DE55R":
    print("\nYou have chosen Planet H01DE55R.\nYou Travel in Light Speed to the planet and land safely to be met by scorching heat and a barren landscape.")
    print("You and your team seem aprehensive about this mission, but you need to proceed, many lives depend on it.")
    choicepath1 = input("You pack water, dehydrated food, and oxygen supply for your team, But you have room for a little more excess material. \n\nChoose your Materials (Type Number):\n1. Pickaxe and Rope\n2. Strange Device\n3. Battle Swords\n4. Puffy Jackets\n5. Nothing, I don't need anything else, I'm brave.\nENTER:")
    #This is the Pixaxe and Rope path
    if choicepath1 == "1":
        pickaxe1 = input("You decide to take the Pickaxe and Rope.\nAs sand and dust pelts you visor, you take a closer look at your immediate surrondings.\nThere is a large crevace in the ground, and you can see a cave entrence looking full to the brim with Precious Gems and Gold.\nOn the other hand, You can see a moutain range in the distance, looking full of life and vegetation, Contrary to the rest of the planet.\nChoose CAVE or MOUNTAINS: ")
        if pickaxe1 == "CAVE":
            print("")
        if pickaxe1 == "MOUNTAINS":
            print("")
    #This is the Strange Device path
    if choicepath1 == "2":
        device1 = input("\nYou Decide to take the Strange Device.\nAs sand and dust pelts you visor, you take a closer look at your immediate surrondings.\nThere is a large crevace in the ground, and you can see a cave entrence looking full to the brim with Precious Gems and Gold.\nOn the other hand, You can see a moutain range in the distance, looking full of life and vegetation, Contrary to the rest of the planet.\nAlternatively, you can activate your strange device now.\nChoose: CAVE | MOUNTAINS | DEVICE: ").upper()
        if device1 == "CAVE":
            print("")
        if device1 == "MOUNTAINS":
            print("")
        if device1 == "DEVICE":
            print("You activate the device, and it teleports you and your team to a different location on the planet.\nYou find yourself in the middle of nowhere, with no landmarks or signs of life.\nNight falls as you wander the dessert. The Planets temperature drops to freezing.\nYou and your team are left with no choice but to huddle together for warmth, and you all die of hypothermia.\nEND")
    #This is the Battle Swords path
    if choicepath1 == "3":
        print("")
    #This is the Puffy Jackets path
    if choicepath1 == "4":
        print("")
    #This is the Nothing path
    if choicepath1 == "5":
        print("")
elif planet == "C01DB1ZD":
    print("\nYou have chosen Planet C01DB1ZD.")
else:
    print("\nInvalid choice. You get sent to unknown coordinates and get lost in the void of space, killing you and your team.\nEND")