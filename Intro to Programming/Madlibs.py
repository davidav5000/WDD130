print ("Welcome to the Madlib Generator!\n")
print ("Please enter the following\n")
adjective1 = input ("Adjective: ")
animal = input ("Animal: ")
verb1 = input ("Verb: ")
exclaimation = input ("Exclaimation: ").upper()
verb2 = input ("Verb: ")
verb3 = input ("Verb: ")
#Adding Variables
print ("")
print (f"Your story is:\n\nThe other day, I was really in trouble. It all started when I saw a very\n{adjective1} {animal} {verb1} down the hallway. {exclaimation}! I yelled. But all\nI could think to do was to {verb2} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb3}\nright in front of my family. ")
#Adding to the story
print (f"\nDo you want to continue the story?")
yesorno = input ("Yes or No: ").lower()
if yesorno == "no":
    print ("Thanks for playing!")
elif yesorno == "yes":
    print ("Please enter the following: ")   
    adjective2 = input ("Adjective: ")
    place = input ("Place: ")
    emotion = input ("Emotion: ")
    color = input ("Color: ")
    date = input ("Date: ")
    adverb = input ("Adverb: ")
    adjective3 = input ("Adjective: ")
    verb4 = input ("(Past Tense) Verb: ")
    verb5 = input ("(Past Tense) Verb: ")
    print (f"\nThe Story Continues...\n\nMy family was in shock as the {adjective1} {animal} then proceeded to {verb4} till \nit was {color} in the face. Suddenly the {animal} became very {emotion}. It {verb4} away \ntowards the {adjective2} {place}. I {adverb} followed it to {place} and {verb5} when I arrived. \nFinally after tracking down the now {adjective3} {animal} I caught it and sent in home. /nThat is what happened on {date}. THE END")
else: 
    print ("Does not Compute. Ending program.")

