#Thomas Boyko Tutorial 08
#ID: 30191728 
#Dungeon of Doom v1 - 09/28/2022
#Features - stores player location and game win state from user input
#displays outputs based on these inputs
#Handles invalid inputs
#Limitations - gameState variable would not work properly in the while loop unless boolean  

#Define necessary constants
WON = True
NOT_WON = False

KITCHEN = 0
PANTRY = 1
ENTRANCE = 2
LIVINGROOM = 3

LEFT = 'left'
CENTER = 'center'
RIGHT = 'right'
OPEN = 1
CLOSED = 0

#Define necessary variables and their initial state
gameState = NOT_WON
playerLocation = ENTRANCE
finalDoor = CLOSED
silverLockState = LEFT
goldLockState = CENTER

#Beginning game text
print("Welcome to the Dungeon of Doom!")
print("You open the door to your home, and as you walk through and shut the door it slams behind you and disappears!")

#Main game loop
while (gameState == NOT_WON):
    #Main game loop
    while (playerLocation == ENTRANCE):
        #Entrance description
        print("""
Room: Entrance
--------------

You are in the entrance to your house. 
In front of you is a closed door, to your left is the door to your pantry,
and to your right is the door to your kitchen

Room actions:
(o)pen the door in front of you
(l)eft to the pantry
(r)ight to the kitchen
              """)
        #Player input
        playerChoice = input("Your selection: ")
        
        #Branching based on player input
        if(playerChoice == "l"):
            playerLocation = PANTRY
        elif(playerChoice == "r"):
            playerLocation = KITCHEN
        elif(playerChoice == "o"):
            #Check state of locks, and determine if the game is won or not
            if (goldLockState == LEFT and silverLockState == RIGHT):
                gameState = WON 
                #The game will continue running if the location is not changed, this would be added regardless in order to continue the game.
                #Having a living room location is necessary at this point to avoid the break command.
                playerLocation = LIVINGROOM
                print("The door slides open smoothly, opening to the rest of the house.")
                print("CONGRATULATIONS! YOU WIN!!!")
            else:
                print("You try to open the door, but it won't budge. \nThere must be some lock keeping it closed, but you can't see anything on the door.")
        else :
            print("ERROR: %s is an invalid input. Please select one of: o, l, r."%(playerChoice))
    
    while (playerLocation == PANTRY):
        #Pantry dialouge and player input.
        print("""
Room: Pantry
------------

You are in your pantry. Nestled in between spices and cereals is a silver lock.
As you begin to play with the lock you notice lines that depict three positions. 
The lock will sit in either a center, left, or right position.
Behind you is the door back to the entrance of the house.

Room actions:
The silver lock is currently set to the %s position.
(l)eft position for the silver lock
(r)ight position for the silver lock
(c)enter position for the silver lock
(d)on't change the lock position and return to the entranceway.
              """%(silverLockState))
        playerChoice = input("Your Selection: ")
        
        #Branching based on player input
        if(playerChoice == "l"):
            silverLockState = LEFT
        elif(playerChoice == "r"):
            silverLockState = RIGHT
        elif(playerChoice == "c"):
            silverLockstate = CENTER
        elif(playerChoice == "d"):
            playerLocation = ENTRANCE
        else :
            print("ERROR: %s is an invalid input. Please select one of: l, r, c, d."%(playerChoice))
    
    while (playerLocation == KITCHEN):
        
        print("""
Room: Kitchen
-------------

You are in the kitchen. Around you is a number of appliances and bowls of produce.
Sitting between the microwave and the sink is a golden lock.
You can see markings on it indicating that it can sit in a center, left, or right position.
Behind you is the door back to the entrance of the house.

Room actions:
The golden lock is currently set to the %s position.
(l)eft position for the gold lock
(r)ight position for the gold lock
(c)enter position for the gold lock
(d)on't change the lock position and return to the entranceway.
              """%(goldLockState))      
        playerChoice = input ("Your Selection: ")
        
        #Branching based on player input
        if(playerChoice == "l"):
            goldLockState = LEFT
        elif(playerChoice == "r"):
            goldLockState = RIGHT
        elif(playerChoice == "c"):
            goldLockState = CENTER
        elif(playerChoice == "d"):
            playerLocation = ENTRANCE
        else :
            print("ERROR: %s is an invalid input. Please select one of: l, r, c, d."%(playerChoice))  
