#Thomas Boyko - 30191728 - T08
#Dungeon of doom 2 - v3 11/03/22
#Features new to v3: Checks for required variables before allowing user to take actions
#ie: previously the user could feed the mouse in the bedroom; the feed option wouldn't show up,
#but the user could still choose it.
#Limitations: named constants were only used for locations, i found that naming variables
#well would help, simplifying so that boolean values could be used.


#define named constants
LIVING_ROOM = 0
ATTIC = 1
BEDROOM = 2
PARADISE = 3

#section for specific room functions

#args (whether the string is in the living room)
#displays the text for the living room
#returns (none)
def livingRoomText(stringInRoom):
        print("Room: Living room")
        print("-----------------\n")
        print("You're in the living room of the house.")
        print("It's tastefully decorated, with artwork decorating the walls.")
        print("In this room you see:")
        if(stringInRoom):
              print("*A ball of string")
        print("*A set of stairs going up")
        print("*A small pot of soil")
        print("*A dark entranceway")
        print("Options:")
        print("(u)p: go up the stairs")
        print("(l)ook: look at the pot of soil")
        print("(g)o: go through the dark entranceway")
        if(stringInRoom):
            print("(t)ake the ball of string")

#args(bool stringTaken, bool playerHasString bool soilReady)
#asks for user input in the living room, and returns output variables based on the choice.
#returns(whether the string is in the room, whether the player has the string, where the player is going next.)
def livingRoom(stringInRoom,playerHasString,soilReady):
    #define a location variable locally, will be outputted to determine where to go.
    location = LIVING_ROOM 
    #main loop for living room
    while (location==LIVING_ROOM):
        #show text, then ask for input
        livingRoomText(stringInRoom)
        userInput = input("Your Selection: ")
        #branching based on user input
        if(userInput == "u"):
           location = ATTIC
        elif(userInput == "l"):
            if(soilReady):
                gameWon = True
                location = PARADISE
            else:
                print("The soil appears dry.")
        elif(userInput == "g"):
            location = BEDROOM
        elif(userInput == "t" and stringInRoom):
            playerHasString=True
            stringInRoom=False
            print("You put the ball of string into your pocket")
        else:
            print("Invalid selection! Try again")
        print('\n')
    #return function outputs
    return stringInRoom,playerHasString,location

#args (whether the player has the string - bool)
#prints attic text
#returns (none)
def atticText(hasString):
    print("Room: Attic")
    print("-----------\n")
    print("This is a rather small attic, filled with more cheese")
    print("than you have ever seen in your life.")
    print("In the attic you also see: ")
    print("*A small hole, smaller than any block of cheese in the room")
    print("*An infinite supply of cheese")
    print("Room actions:")
    print("(c)heese: take some cheese and immediately try to dop it in the hole")
    if (hasString):
        print("(s)tring: drop the string that's in your pocket into the hole.")
    print("(p)ickup: pick up some cheese and keep it.")
    print("(d)own: go down the stairs\n")

#args(whether the player has the string, how much cheese the player has,whether the cat is in the bedroom)
#asks for attic input, then returns variables based on choice
#returns(whether the player has string, how much cheese the player has,whether the cat is in the bedroom)
def attic(hasString,playerCheese,catInBedroom):
    #define local main looping variable, will become false when the player chooses to leave the room
    inAttic = True
    while(inAttic):
        #print attic text then ask for input
        atticText(hasString)
        userInput = input("Your Selection: ")
        #branching based on user input
        if(userInput == "c"):
            print("The cheese is too big to be put in the hole.")
        elif(userInput == "s" and hasString):
            hasString = False
            catInBedroom = False
            print("The string rolls down the hole and out of sight.")
            print("You hear joyful meowing coming from another room.")
        elif(userInput == "p"):
            playerCheese+=1
            print("You take some cheese. You now have %d cheese"%playerCheese)
        elif(userInput == "d"):
            inAttic = False
        else:
            print("Invalid selection! Please try again!")
        print('\n')
    return hasString,playerCheese,catInBedroom

#args(bool: player has string, bool: cat is in room, int: playerCheese)
#displays text in the bedroom
#returns(none)
def bedroomText(hasString,catInRoom,playerCheese):
    print("Room: Bedroom")
    print("-------------\n")
    print("The bedroom is simple, hosting a bed, dresser,")
    print("and a locked doorway that you assume goes to an en")
    print("suite bathroom.")
    print("In the bedroom you also see: ")
    print("*A small hole in the baseboards, likely housing a mouse.")
    if(catInRoom==True):
        print("*A tomcat, staring intently at the hole in the baseboards.")
    if (catInRoom ==False):
        print("*A mouse, come out of its hole, shivering and hungry.")
    print("*The dark entranceway, leading back to the living room.")
    print("Room options:")
    print("(b)ack: Go back through the dark entranceway")
    if(hasString and catInRoom):
        print("(p)lay: play with the tomcat using the string in your pocket")
    if (catInRoom == False and playerCheese>0):
        print("(f)eed: feed some cheese to the mouse")
    
#args(whethere the player has string, cat is in room, player cheese amount.)
#recieves input from the user and then modifies variables and returns them
#returns(soilFertilized)
def bedroom(hasString,catInRoom,playerCheese,soilFertilized):
    #local variable used for looping again, this will be false when the player chooses to leave
    inBedroom = True
    while inBedroom:
        #Prints bedroom text then requests user input
        bedroomText(hasString,catInRoom,playerCheese)
        userInput = input("Your Selection: ")
        #branching based on user input
        if(userInput == "b"):
            inBedroom = False
        elif(userInput == "p" and hasString and catInRoom):
            print("You roll the ball of string to the tomcat.")
            print("It paws the string a few times, then rolls it back to you bored.")
        elif(userInput == "f" and catInRoom==False and playerCheese>0):
            print("You break off a piece of cheese and feed it to the mouse.")
            print("The mouse scurries to the living room, as if it's doing a \"potty dance\",")
            print("then comes back, looking up at you for more cheese.")
            soilFertilized=True
        else:
            print("Invalid selection! Please try again!")
        print('\n')
    return soilFertilized

    

#args(none)
#returns(none)
#starting function to the program
def start():
    #define local variables to the start function
    gameWon = False
    location = LIVING_ROOM
    playerCheese = 0
    stringInLivingRoom = True
    playerHasString = False
    catInBedroom = True
    soilFertilized = False

    #main game loop
    while not (gameWon):
        #check player location and run the appropriate function
        #Note: if the player is in the attic or bedroom, there is only one way for them to go, so after they leave the room,
        #their location is automatically set to the living room.
        if(location == LIVING_ROOM):
            stringInLivingRoom,playerHasString,location = livingRoom(stringInLivingRoom,playerHasString,soilFertilized)
        if(location == BEDROOM):
            soilFertilized = bedroom(playerHasString,catInBedroom,playerCheese,soilFertilized)
            location = LIVING_ROOM
        if(location == ATTIC):
            playerHasString,playerCheese,catInBedroom = attic(playerHasString, playerCheese, catInBedroom)
            location = LIVING_ROOM
        if(location == PARADISE):
            gameWon = True
    #once the main loop breaks, we print the winning text and the start function ends.            
    print("A vine grows from the plant in the pot, and you climb it up to paradise!")
    print("You've won Dungeon of Doom v2!")
#call start function
start()
