## Why?
Generation of Npc Attribtrues are just a pain to deal with while creating Npcs. With this Program, I aim to make you life just a bit easier. This program can generate Characteristics for an Npc... The Name, Strength, Speed, IQ, and Size.

## How Do I Run It?
Simply open the project with codespaces. Next, in the terminal, type "python3 Npc_Generator.py".

## How Do I Use It?
Upon Running The Program, you will be asked to type "true" to start. So, to begin, simply type "true". Next type a whole, integer number, for the amount of NPCs you would like to generate. If the amount it 1, then you may choose a name for the Npc, but any amount greater than 1 will result in a random name. The program will then print the Npcs information in the following format:
NpcNumber
 Attributes:
 Attribute1 = ___
 Attribute2 = ___
 Attribute3 = ___
 Attribute4 = ___

## Configuring?
This program in made in a very simple and configurable fasion. You can add more names to the random name list, add attributes, change ranges in which the attributes are assigned numbers or amounts.

## Altering Random Names
To alter the random names, first simply open the Npc_Generator.py file. Next find the list of random names. It should look like this,
names = ["Kavin", "Eyad", "Nick", "Jayden", "Azaan", "Ethan", "Leo"]
To add more names, add a ", "Name here" "
Ex:
names = ["Kavin", "Eyad", "Nick", "Jayden", "Azaan", "Ethan", "Leo", "Namehere"]
To remove a name, remove the ", "Nick" "
Ex:
names = ["Kavin", "Eyad", "Jayden", "Azaan", "Ethan", "Leo"]

## Adding Attributes
To alter the random names, first open the Npc_Generator.py file. Next find the list of attributes. It should look like this,


        Attribute1 = random.randint(1, 8)
        Attribute2 = random.randint(1, 100) + 0.00
        Attribute3 = random.randint(1, 250)
        Attribute4 = random.randint(1, 100) + 0.00
        IsFriendly = random.choice([True, False])


and the print statment which should be 2 lines under it,


        print(f"Npc#{NpcNumber} \n Attributes: \n Name = {NpcName} \n Attribute1 = {Attribute1} \n Attribute2 = {Attribute2} \n Attribute3 = {Attribute3} \n Attribute4 = {Attribute4} \n IsFriendly = {IsFriendly}")


To add a new attibute, simply make a new variable in this format and add it under the other varibles,


        NewAttribute = random.randint(num1, num2) + 0.00 (add + 0.00 to turn it into a float)


or like this


        IsCool = random.choice([True, False])
        

Next, add it into the print statment like this,

        print(f" \n NewAttribute = {NewAttribute} ")

or like this,

        print(f" \n IsCool = {IsCool} ")

It should look like this,
Attribute1 = random.randint(1, 8)
        Attribute2 = random.randint(1, 100) + 0.00
        Attribute3 = random.randint(1, 250)
        Attribute4 = random.randint(1, 100) + 0.00
        NewAttribute = random.randint(1, 100) + 0.00
        IsFriendly = random.choice([True, False])
        isHostile = random.choice([True, False])
        print(f"Npc#{NpcNumber} \n Attributes: \n Name = {NpcName} \n Attribute1 = {Attribute1} \n Attribute2 = {Attribute2} \n Attribute3 = {Attribute3} \n Attribute4 = {Attribute4} \n NewAttribute = {NewAttribute} \n Friendly = {IsFriendly} \n Cool = {IsCool}")

And yes you can change the names of the variables to what every you want.


Example Output:

Type 'true' to begin!: true
How many Npcs?: 2
Npc#1 
 Attributes: 
 Name = Leo 
 Attribute1 = 7 
 Attribute2 = 63.0 
 Attribute3 = 92 
 Attribute4 = 99.0 
 IsFriendly = False
Npc#2 
 Attributes: 
 Name = Nick 
 Attribute1 = 4 
 Attribute2 = 97.0 
 Attribute3 = 174 
 Attribute4 = 77.0 
 IsFriendly = True
All Npcs Have Been Generated!