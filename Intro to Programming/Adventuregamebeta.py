#adventure game start
print ("Welcome to the Choose your own Adventure Game! (Space Edition)")
#ASCII art of Planet
print ("\n *       .         * .::.\n         *        .:'  .:\n   .    ,MMM8&&&.:'   .:'   *\n       MMMMM88&&&&  .:'\n*     MMMMM88&&&&&&:'\n      MMMMM88&&&&&&      *\n    .:MMMMM88&&&&&&  <■■=# .\n* .:'  MMMMM88&&&&\n.:'   .:'MMM8&&&'     *\n:'  .:'  .         .        *\n'::'       *\n")
print ("\nYou are a space explorer captain on a mission to find a new planet for humanity. \nEarth has become uninhabitable, and your task is to find a suitable replacement.")
print("\nYou have chosen Planet H01DE55R.\nYou travel in light speed to the planet and land safely to be met by scorching heat and a barren landscape.")
print("\nYou and your team seem aprehensive about this mission, but you need to proceed, many lives depend on it.")
choicepath1 = input("\nYou pack water, dehydrated food, and oxygen supply for your team, But you have room for a little more excess material. \n\nChoose your Materials (Type Number):\n1. Pickaxe and Rope\n2. Battle Swords\n3. Nothing, I'm Brave\n\nENTER: ")
if choicepath1 == "1":
        pickaxe1 = input("\nYou decide to take the Pickaxe and Rope.\nAs sand and dust pelts your visor, you take a closer look at your immediate surrondings.\nThere is a large crevace in the ground, and you can see a cave entrence looking full to the brim with precious gems and gold.\nOn the other hand, You can see a moutain range in the distance, looking full of life and vegetation, Contrary to the rest of the planet.\n\nChoose: CAVE or MOUNTAINS: ").upper()
        if pickaxe1 == "CAVE":
            cave1 =input('\nAs you enter maw of the cave, you tie your rope to the entrance post so you can find your way back.\nAs you veture deeper, you notice that the cave walls are lined with ancient alien hyeroglyphs.\nOne you your team members take a look and attempts to decipher them.\n\n["The gyphs say:] \n\nG̵̛̞͂͋̒̕ͅa̷̫̯̫͖̅̑̋r̴̬̲̦̻̃̔̾g̷̮̺̾͊o̷̢͕͂͂̓r̷̟̠͍̭͚̓̊̑͆ǫ̶̢̻̲̒͐̆̽ț̶͊̔͆͜h̵̡̜̹͎̝̽̀̉  the ancient being is p̵̭̬͕̘̣͓͓͉̈́͋̓́̓̌̓̽̌͑̄̏͝͠͠ͅr̵̡̘̞̼̝̣̯̫̠̞̣̦̬͌͝o̸̧̧̦͓̫̔̃̌͛͛̈͠ẗ̸̡̛́̓̇ĕ̸̛͙̺̼͙c̶̨̣̗̝̦͎̒̔̀̓͊͆̊̀͐̋̉͝͝ͅţ̴̯͈̰̿̍̈̊̈́̏̾i̵̖̮͉̤̦̥̩͈͇̎͆͌̈́́̃̐̈́̀͠ͅn̸̢̛̠̟̗̝̗͖̹̝̆̿͐̄͐͆̇͂̓̿̑̐͘g̷̛̙̻̝̱̳͂̀̑͊̀ͅ the t̵͍͍̏r̷̰̯͒ĕ̴͔ȧ̴͜s̴̝̹̄̔u̸̥̿̀r̷͔̻͐̎e̸̤͋ of this t̸͎̣͗ọ̸̃͜m̸̞͓̉̕b̶̦̠̕. \n[Much of this is illegible due to its old and decrepid nature."]\n\nWith that in cosideration you are faced with a choice. Mine the GEMS using the pickaxe, or PLUNDER the cave further in search of GOLD.\nChoose: GEMS | PLUNDER: ').upper()
            if cave1 == "GEMS":
                gems1 = input('\nAs you are swinging your pickaxe and harvesting the gems, your team gathers the forgien material for further investigation.\nA deep bellowing growl echos from deep in the cave, frightening the team.\n["We should cut our losses and get out of here!"]\n["NO! This is precious data, we still have time!"]\nChoose: STAY | LEAVE: ').upper()
                if gems1 == "LEAVE":
                    leave1 = input("\nGrabbing a handful of gems, you and your team make a run for it.\nAs you reach the entrance, the growl turns into a roar, and a giant alien creature emerges from the cave.\nWith you being ahead and running towards your ship, you manage to board as the creature composes itself, clearly not accustomed to the light of the surface.\nWhile you have the oportunity to escape, you remember your directive. Is what you accomplished sufficient? What will you do?\nChoose: ESCAPE | FIGHT: ").upper()
                    if leave1 == "ESCAPE":
                        #ENDING 1 RENEWED EARTH
                        print("\nYou and your team escape the planet with the gems, and return to earth.\nIt is discoved that the alien gems contain high amounts of energy, and is thus harnessed to aid in the global energy crisis.\nThe Earth is again restored with this new found technology, making way for renewable and clean energy.\nYou and your team are hailed as heros.\n\nENDING 1: RENEWED EARTH\n----------------------------------")
                    elif leave1 == "FIGHT":
                        print("\nWhile the beast is stunned you and your team decide to engage in combat.\nYou swing your pickaxe at the beast. Nothing.\nYou throw a gem at the beast. Nothing.\nThe Beast ajusts to the light and promtly crushes you and your team into the ground.\n\nEND")
                    else:
                        print("Invalid input. Try again")
                elif gems1 == "STAY":
                    print("\nYou stay to collect more gems. The gowls turn to roars, and soon a firgure emerges from the depths of the cave.\nYou and your team are left speachless as the beast rears its jaw towards you\nWith the weight of the gems slowing you down for any chance of escape, you and your team are brutally slaughtered.\n\nEND")
                else:
                    print("Invalid input. Try again")
            elif cave1 == "PLUNDER":
                plunder1 = input('\nPassing by the shiny gems, your heart is set on plundering the cave of its riches.\nOne of your team members protests; claiming...\n["This is foolish, remember the directive captain? How will this benifit Earth!"]\nChoose: IGNORE | SCOLD: ').upper()
                if plunder1 == "IGNORE":
                    ignore1 = input("\nYou proceed to ingore the insulant team member.\nHe gets the hint, and with no other choice of survival, your team continues to follow you deeper.\nYou enter into a chamber with a unidentifiable large alien creature slumbering atop a pile of RICHES.\nThere is also an Gilded BOX of some kind to the left side of the room.\nChoose: RICHES | BOX: ").upper()
                    if ignore1 == "RICHES":
                        print("\nYou make your way to the pile of riches; your heart fully set on greed.\nOne of your clumsy teamates trips over an alien chalice, causing a slew of ornaments to slide down from the pile.\nThe alien creature immediately awakens to the loud cacophany, foiling the stealth mission.\nWithout so much as a word he gobbles up your teamates, leaving you for desert for his three course meal.\n\nEND")
                    elif ignore1 == "BOX":
                        box1 = input("\nYou carfully make your way to the gilded box.\nYour teamates have fully lost faith in you and are frozen by the chamber's exit.\nYou open the box and discover the mummified remains of an alien royalty, signified by a spotless, bejeweled, tempting crown\nBy almost second instint you dawn the crown.\nGargoroth is now at your command.\nChoose: RULE | RELINQISH: ").upper()
                        if box1 == "RULE":
                            #ENDING 2 NEW ORDER
                            print("\nYou take control of the crown and its accociated authority.\nAll the creatures of the planet obey your command including the powerful Gargoroth.\n Your team sighs relief as they re-instate thier trust in thier captain, and now king.\nYour new world order gives you dominace over the planet, thus conquering and finding a suitable new earth, with you at the helm.\nMISSION ACCOMPLISHED\n\nENDING 2: NEW ORDER\n----------------------------------")
                        elif box1 == "RELINQUISH":
                            print("\nYou decide that the power isn't worth it.\nYou remove the crown only to be met with a swipe to the chest from Gargoroth.\n\nN̵͈̞͍̾́̌̐͐̇͝O̷̧͓̲͐̔̀͛̾̈̊͂̇͠Ṭ̸̬͕̙̻͈̲̊̈͌̌͒ ̵͕̺̘̓̈̃̎̈́̃̊͝W̶̗̳͗̽Ơ̴͇̠̾̂̾́̇̕͘R̵̠̹̙͖͉͖͆̌͆T̶̛̙̻͙̗̙̭͑̈͗H̸͙̝̀́̓̀͐͐̈́̇Ý̷̫͈̰͋\n\nEND")
                        else:
                            print("Invalid input. Try again")
                    else:
                        print("Invalid input. Try again")
                elif plunder1 == "SCOLD":
                    scold1 =input("\nYou scold your team member for questioning your reasoning.\nYou are the Captain after all...\nWhen all of a sudden, an alien beast stands before you and your team, likely attracted by the loud scolding.\nThe beast speaks in an alien toungue, with you only able to make out one word...\n[G̵̛̞͂͋̒̕ͅa̷̫̯̫͖̅̑̋r̴̬̲̦̻̃̔̾g̷̮̺̾͊o̷̢͕͂͂̓r̷͍̭͍̃̊͑͆͟ǫ̶̢̻̲̒͐̆̽ț̶͊̔͆͜h]\n\nYou and your team are left with no choice but to fight or take flight.\nChoose: FIGHT | RUN: ").upper()
                    if scold1 == "FIGHT":
                        print("\nYou attempt to fight the beast.\nYou swing you pickaxe at the beast, but it's scaley exterior deflects the blow.\nYou call for your team to back you up, but they have all fled to the surface, leaving you a dead man.\nThe beast swallows you whole, as you reconsider your life choices and priorities.\n\nEND")
                    if scold1 == "RUN":
                        run1 = input("\nAs you feel the beasts heavy breath rest upon your face, you turn tail and make a run for it, not looking back for a second.\nSomehow, you managed to make it outside the cave, although your team doesn't follow suit.\n You are left to youself.\nChoose: RESCUE | FLEE: ").upper()
                        if run1 == "RESCUE":
                            print('\nFeeling somewhat responsible for your teams health and saftey, you return to the cave, following the rope you tied to the entrance.\nYou find your team alright, just not quite all "together".\nThe Beast stands over the carcasas looking like it just had an appetizer.\nYou make eye contant with the beast and it hunts you down. You die with somewhat remorse.\n\nEND')
                        if run1 == "FLEE":
                            print("\nYour dignity and backbone now stripped, you flee to your ship.\nUnfortunatley the ship needs a team to operate and lift off, leaving you stranded as you slowly consume all the dehydrated space noodles in the cupboards.\nYou die a cowards death as you huddle in your ship, starving to death.\n\nEND")
                else:
                    print("Invalid input. Try again")
            else:
                print("Invalid input. Try again")                
        elif pickaxe1 == "MOUNTAINS":
            mountain1 =input("\nYou opt to go towards the moutains.\nAs you journey your way over to the range, the planets temperature begins to drop due to the planets sun setting.\nBy now you've made it to the lush foothills.\nChoose: CAMP | HIKE: ").upper()
            if mountain1 == "CAMP":
                camp1 =input("\nUsing the dry folliage and alien tree branches, you manage to light a fire, keeping your team warm through the night.\nIn the morning, You recouperate, take heading, and continute your way though the alien jungle.\nYou are stopped by a sheer cliffside.\nChoose: CLIMB | SEARCH: ").upper()
                if camp1 == "CLIMB":
                    climb1 =input('\nUsing your Pickaxe and Rope, You and your team scale the cliffside succesfully.\nOn top of the plateau, you find a spring of liquid.\nIts crystal clear and fresh to the touch.\n["This might be water!"]\nChoose: DRINK | COLLECT: ').upper()
                    if climb1 == "DRINK":
                        print('\nYou remove your visior, finding the enviroment to be oxygen rich.\nYou take a sip of the delectable spring.\nImmediately the liquid corrodes your insides and leaves a hole through you small intestine.\nYour team panics to apply first aid, but its pretty "clear" you wont make it.\nMaybe drinking the jungle juice was a bad idea...\n\nEND')
                    elif climb1 == "COLLECT":
                        collect1 =input("\nOne of your teamates hands you a flask\nYou collect the liquid.\nYou continue walking on the plateau. A herbivorous creature approaches you, but can tell its friendly.\nIt has fuzz everywhere except its underbelly, and big horizontal pupils, much like the goat of your homeworld.\nYou are enermored by its almost cute demenor.\nIt is attracted to the flask of liquid you collected.\nChoose: QUENCH | REFUSE: ").upper()
                        if collect1 == "QUENCH":
                            #ENDING 3 Domestication
                            print('\nYou give the liquid to the alien to drink.\nIt eagerly partakes and makes a loud "EH-EH-EH-EH" sound echoing through the jungle.\n The creatures heard is summoned by the call and are immediatley docile to you and your team, almost domesticated.\n You also make the conclusion that these animals are producing purified water through thier glands and are the ones responsible for this mini ecosystem and makeshift atmosphere.\n["This is the place captain, we can establish civilization here!]\nWith confimation from your team, you make contanct with earth and report.\nMISSION SUCCESFUL\n\nENDING 3: DOMESTICATION\n----------------------------------')
                        elif collect1 == "REFUSE":
                            print("\nThe Alien presses up agaisnt you, insistent on obtaining the flask.\nYou hold it up high above your head, but the alien jumps on your torso, crushing your ribs.\nYou bleed out. Your team tires to provide first aid, but to no avail. The Alien drinks from the broken flask.\n\nEND ")
                        else:
                            print("Invalid input. Try again")
                    else:
                        print("Invalid input. Try again")
                elif camp1 == "SEARCH":
                    search1 = input("Looking for an alternative route, pushing past the foliage, you find a pathway leading to what look like ancient ruins\nThese structures are long abandoned, and ancient characters line the pillars and crumbled walls.\nOne such gyph depicts a humanoid figure bringing Gold and Riches to an alter.\nThe Alter stand before you.\nChoose: OFFERING | LEAVE: ").upper
                    if search1 == "OFFERING":
                        print('\nYou Attempt to offer GOLD, but you dont have any GOLD.\nIt is only until now you notice that one of your teamates have stepped on a pressure pad.\n["Uh Oh.."]\nA slew of hidden dart traps pierce you and you team; you feel very sleepy. You dont wake up.\n\nEND')
                    elif search1 == "LEAVE":
                        print('\nYou walk away, When you suddenly hear a click sound...\nYou look at you foot on top of a pressure pad.\nA slew of hidden dart traps pierce you and you team; you feel very sleepy. You dont wake up.\n\nEND')
                    else:
                        print("Invalid input. Try again")
                else:
                    print("Invalid input. Try again")
            if mountain1 == "HIKE":
                print("\nDepite the cold and darkness, your team press forward.\nQuite predictably, The temperature drops below freezing, putting you and your team in shock; suffering from hypothermia.\nYou make it to a cliffside before you passout on the alien jungle floor.\n\nEND ")
            else:
                print("Invalid input. Try again")
        else:
            print("Invalid input. Try again")
    #This is the Battle Swords path
elif choicepath1 == "2":
        swords1 = input("\nYou decide to equip the Battle Swords.\nAs sand and dust pelts your visor, you take a closer look at your immediate surrondings.\nThere is a large crevace in the ground, and you can see a cave entrence looking full to the brim with precious gems and gold.\nOn the other hand, You can see a moutain range in the distance, looking full of life and vegetation, Contrary to the rest of the planet.\nChoose: CAVE or MOUNTAINS: ").upper()
        if swords1 == "CAVE":
            cave3 =input("\nYou branish your swords, passing by the crystalized gems iluminating the entrance.\nYou make your way deeper in the cave with a stoic look on your face.\nYou enter into a chamber with a unidentifiable large alien creature slumbering atop a pile of RICHES.\nChoose: STEATH | CHALLENGE: ").upper()
            if cave3 == "STEATH":
                print("\nYou attempt to sneak around with your team, feeling confident.\nWhen out of nowhere one of your team members trip over a gold chalice and awaken the strange creature.\nThe alien speaks in an unknown tounge, but you can make out the word G̵̛̞͂͋̒̕ͅa̷̫̯̫͖̅̑̋r̴̬̲̦̻̃̔̾g̷̮̺̾͊o̷̢͕͂͂̓r̷̟̠͍̭͚̓̊̑͆ǫ̶̢̻̲̒͐̆̽ț̶͊̔͆͜h̵̡̜̹͎̝̽̀̉\nhaving been not prepared to fight, he lands the first blow on your team, knocking you all unconscious. You will surely be eaten.\n\nEND")
            elif cave3 == "CHALLENGE":
                challenge1 = input("\nYou take stance with your team, preparing for a fight.\nYou awaken the Beast and openly challenge him, drawing your swords.\nThe Beast with no hesitation attempts to make a strike, but you evade.\nIt attempts again, and you evade again.\nIt attempts one more time but is slower than before. You and your team find an opening between it scales\n*SLICE*\nThe Beast bleeds out and rampages at you before losing conciousness, falling on a BOX to its left.\nYou Have Conquered Gargoroth.\nChoose: GOLD | CELEBRATE: ").upper()
                if challenge1 == "GOLD":
                    gold1 =input("\nYou collect the GOLD.\nYou exit the cave having now obtained your loot.\nHave you achived your mission?\nChoose: MOUNTAINS | HOME: ").upper()
                    if gold1 == "MOUNTAINS":
                        mountain2 =input("\nYou opt to go towards the moutains.\nAs you journey your way over to the range, the planets temperature begins to drop due to the planets sun setting.\nBy now you've made it to the lush foothills.\nChoose: CAMP | HIKE: ").upper()
                        if mountain2 == "CAMP":
                            camp2 =input("\nUsing the dry folliage and alien tree branches, you manage to light a fire, keeping your team warm through the night.\nIn the morning, You recouperate, take heading, and continute your way though the alien jungle.\nYou are stopped by a sheer cliffside.\nChoose: CLIMB | SEARCH: ").upper()
                            if camp2 =="CLIMB":
                                print("\nYou try to climb the sheer cliff.\nAt about 25ft, your lose your grip and fall to the floor. You Splat.\n\nEND")
                            elif camp2 =="SEARCH":
                                search2 =input("\nLooking for an alternative route, pushing past the foliage, you find a pathway leading to what look like ancient ruins\nThese structures are long abandoned, and ancient characters line the pillars and crumbled walls.\nOne such gyph depicts a humanoid figure bringing GOLD and Riches to an alter.\nThe Alter stand before you.\nChoose: OFFERING | LEAVE: ").upper()
                                if search2 == "OFFERING":
                                    #ENDING 4 KING OF H01DE55R
                                    print('\nYou offer up the GOLD you obtained from the cave to the alter.\nA group of pygmy like aliens emerge from the lush bushes. Seeing as in thier eyes you have fufilled thier prophecy, they bow to you as thier new king.\nYou and your team find this benificial as they introduce you to thier society as a monarch.\n["We can form an allience with this group of aliens and make this planet habiable!"] says one of your team members.\nWhile they have a pygmy like culture, thier technology is far above what we are capable of.\nThe melding of these two great societies will flourish!\n\nENDING 4: THRIVING ALLIANCE\n----------------------------------')
                                elif search2 == "LEAVE":
                                    print('\nYou walk away, When you suddenly hear a click sound...\nYou look at you foot on top of a pressure pad.\nA slew of hidden dart traps pierce you and you team; you feel very sleepy. You dont wake up.\n\nEND')
                                else:
                                    print("Invalid input. Try again")
                            else:
                                print("Invalid input. Try again")
                        elif mountain2 == "HIKE":
                            print("\nDepite the cold and darkness, your team press forward.\nQuite predictably, The temperature drops below freezing, putting you and your team in shock; suffering from hypothermia.\nYou make it to a cliffside before you passout on the alien jungle floor.\n\nEND ")
                        else:
                            print("Invalid input. Try again")
                    elif gold1 == "HOME":
                        #ENDING 5: RICHES, AT WHAT COST...
                        print('\nYou and your team decide to head back home.\nWhen you return to the dying earth, The Govenment asks what was achived.\nYou show the plethora of gold to your higher ups, only to be met with confusion.\n["YOU HAVE FAILED YOUR MISSION. YOU SOUGHT ONLY AFTER RICHES! YOU ARE FIRED!!!"]\n\nENDING 5: RICHES, AT WHAT COST...\n---------------------------------- ')
                    else:
                        print("Invalid input. Try again")
                elif challenge1 == "CELEBRATE":
                    print("\nYou all take a moment to celebrate, letting out a war cry for your triumph.\nUnfortunately, you hadn't noticed the intergrity of the chamber was serverly damaged after the fight.\n The echos of the war cries cause the chamber to collapse, crushing you, your team, and the Beast in the process.\nMaybe the celebration was a little preemtive..\n\nEND")
                else:
                    print("Invalid input. Try again")
            else:
                print("Invalid input. Try again")
        elif swords1 == "MOUNTAINS":
            mountain3 =input("\nYou opt to go towards the moutains.\nAs you journey your way over to the range, the planets temperature begins to drop due to the planets sun setting.\nBy now you've made it to the lush foothills.\nChoose: CAMP | HIKE: ").upper()
            if mountain3 == "CAMP":
                camp3 =input("\nUsing the dry folliage and alien tree branches, you manage to light a fire, keeping your team warm through the night.\nIn the morning, You recouperate, take heading, and continute your way though the alien jungle.\nBut before you leave camp, An alien enemy arachnid jumps you and your team.\nChoose: SLAY | BEFRIEND: ").upper()
                if camp3 == "SLAY":
                    slay =input("\nYou slash your sword right through the spider-alien.\nThere is something hard in the middle of the dismembered alien\nYou obtain the Strange Object.\nYou continue on your way though the alien jungle.\nYou are stopped by a sheer cliffside.\nChoose: CLIMB | SEARCH: ").upper()
                    if slay == "CLIMB":
                        print("\nYou try to climb the sheer cliff.\nAt about 25ft, your lose your grip and fall to the floor. You Splat.\n\nEND")
                    elif slay == "SEARCH":
                        search3 =input("\nYou search around the cliffside, when you notice a small concave slot in the face of the cliff.\nYou decide to insert the object you got from the spider, noticing it fits perfectly.\nA door opens after you insert it.\nChoose: ENTER | CLIMB: ").upper()
                        if search3 == "ENTER":
                            #ENDING 6: AMBASSADORS
                            print("You enter the door with your team\nYou find an entire underground civilization of aliens who are curious of your entry.\nThey have advanced technology and seem to be peaceful!\nThey cautiously welcome you in and take you and the team to what you assume is thier leader.\nThey celebrate your arrival! and offer you citizenship in thier city.\n Hopefully you and your team can be good ambassadors, and in time introduce more humans onto thier planet.\n\nENDING 6: AMBASSADORS\n----------------------------------")
                        elif search3 == "CLIMB":
                            print("\nYou try to climb the sheer cliff.\nAt about 25ft, your lose your grip and fall to the floor. You splat as a group of aliens watches you from the door you opened.\n\nEND")
                        else:
                            print("Invalid input. Try again")
                elif camp3 == "BEFRIEND":
                    print("\nYou attempt to befriend the spider-like creature\nIt bites you in the face, and your head swells up like blueberry.\nI thought you were a fighter, not a lover!\n\nEND")
                else:
                    print("Invalid input. Try again")                   
            elif mountain3 == "HIKE":
                print("\nDepite the cold and darkness, your team press forward.\nQuite predictably, The temperature drops below freezing, putting you and your team in shock; suffering from hypothermia.\nYou make it to a cliffside before you passout on the alien jungle floor.\nThose swords really helped huh.\n\nEND ")
            else:
                print("Invalid input. Try again")
        else:
            print("Invalid input. Try again")
elif choicepath1 == "3":
    print('"Ha! like I need extra stuff!"\nAlmost by pure karma for your arrogance, a meteor plummets to the surface of the planet, destroying everything in sight.\nIncluding your ego.\n\nENDING 7. ARROGANCE\n----------------------------------')
else:
    print("Invalid input. Try again")
    