## NPC GENERATION SYSTEM

## Importing Needed Libraries
import time
import random

## List of Random Names
names = ["Kavin", "Eyad", "Nick", "Jayden", "Azaan", "Ethan", "Leo"]
## Asking for True or False input.
isCreating = input("Type 'true' to begin!: ")
## Integer input for the amount of npcs
amount = int(input("How many Npcs?: "))
## Checking if user inputted true for isCreating
if isCreating:
    ## for loop to create the nessesary amount of Npcs
    for i in range(amount):
        ## Gives the Npc A Number Base On The Iteration
        NpcNumber = i + 1
        ## Gives NPC a Random Name.
        NpcName = random.choice(names)
        ## Adds a 500 milisecond pause
        {time.sleep(0.5)}
        ## Prints the Npc's Information, such as Number, Name, and Attributes
        print(f"Npc#{NpcNumber} \n Attributes: \n Strength = {random.randint(1, 100)} \n Speed = {random.randint(1, 100)} \n IQ = {random.randint(1, 250)} \n Size = {random.randint(1, 8)}")
        ## Adds a 500 milisecond pause
        {time.sleep(0.5)}
    ## Sets isCreating to false to prevent the loop from running again.
    isCreating = False
## Final print statment confirming that the all Npcs have been generated.
print("All Npcs Have Been Generated!")