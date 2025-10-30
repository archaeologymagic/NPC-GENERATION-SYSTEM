## NPC GENERATION SYSTEM

## Importing Needed Libraries
import time
import random

## List of Random Names
names = ["Kavin", "Eyad", "Nick", "Jayden", "Azaan", "Ethan", "Leo"]
## Asking for True or False input.
isCreating = input("Type 'true' to begin!: ")
## Checking if user inputted true for isCreating
if isCreating == "True" or isCreating == "true":
    ## for loop to create the nessesary amount of Npcs
    ## Integer input for the amount of npcs
    amount = int(input("How many Npcs?: "))
    for number in range(amount):
        ## Gives the Npc A Number Base On The Iteration
        NpcNumber = number + 1
        ## Gives NPC a Random Name.
        NpcName = random.choice(names)
        ## Adds a 500 milisecond pause
        {time.sleep(0.5)}
        ##Attributes:
        Attribute1 = random.randint(1, 8)
        Attribute2 = random.randint(1, 100) + 0.00
        Attribute3 = random.randint(1, 250)
        Attribute4 = random.randint(1, 100) + 0.00
        IsFriendly = random.choice([True, False])
        ## Prints the Npc's Information, such as Number, Name, and Attributes
        print(f"Npc#{NpcNumber} \n Attributes: \n Name = {NpcName} \n Attribute1 = {Attribute1} \n Attribute2 = {Attribute2} \n Attribute3 = {Attribute3} \n Attribute4 = {Attribute4} \n IsFriendly = {IsFriendly}")
        ## Adds a 500 milisecond pause
        {time.sleep(0.5)}
    ## Sets isCreating to false to prevent the loop from running again.
    isCreating = False
    print("All Npcs Have Been Generated!")
else:
    print("Invalid Input, Please Restart The Program And Type 'true' To Begin.")
## Final print statment confirming that the all Npcs have been generated.