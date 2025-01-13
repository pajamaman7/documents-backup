#Thomas Boyko - T08 - 30191728
#Game of life program v2 - 30/11/22
#Features: can handle any dimensions of input from a file, as well as the 6 premade beginning states. 
#rewrote the oneEmpty function to help with initializing newWorld at the start of the turn, and edited 
#all the functions for allow for any list dimensions.
#Limitations: debug mode currently has no function

#Define named constants
EMPTY = " "
CRITTER = "*"
SIZE = 10
END_OF_LINE = ""
NEWLINE = "\n"
debugOn = False

#Arguments (2d list of the world, row to check, column to check)
#Checks the number of critters surrounding a certain cell.
#Returns (int: how many critters)
def crittersAround(oldWorld, row, column):
    critters = 0
    numRows, numColumns = findDims(oldWorld)
    #These range functions generate a range (-1,0,1) so that we can check all eight entries around a cell
    for i in range(-1,2):
        for j in range(-1,2):
            #avoids errors from the program checking indexes outside of a list.
            if row+i in (-1,numRows) or column+j in (-1, numColumns):
                continue
            if oldWorld[row+i][column+j]==CRITTER:
                critters += 1
    #This last check is to make sure the cell being checked doesn't add to the count of critters around it.
    if oldWorld[row][column] == CRITTER:
        critters -= 1
    return critters

#Arguments(list newWorld)
#what was newWorld will become oldWorld, and newWorld will be modified according to Conway's game of life.
#Returns(oldWorld,newWorld)
def updateWorld(newWorld):
    oldWorld = newWorld
    rows, columns = findDims(oldWorld)
    newWorld = oneEmpty(rows, columns)
    for r in range(0,rows):
        for c in range(0,columns):
            critters = crittersAround(oldWorld,r,c)
            #branching based on the number of critters around
            #first, death conditions:
            if (oldWorld[r][c] == CRITTER and (critters <= 1 or critters >=4)):
                newWorld[r][c] = EMPTY
            #next, birth conditions
            elif(oldWorld[r][c] == EMPTY and critters == 3):
                newWorld[r][c] = CRITTER
            #finally, the catch-all
            else:
                newWorld[r][c] = oldWorld[r][c]
                
    return oldWorld,newWorld

#Args(none)
#Displays the choices for the player's starting world
#Returns(none)
def displayStartText():
    print("Choices for starting biospheres: ")
    print("\t(1) Empty")
    print("\t(2) Single critter")
    print("\t(4) Simple birth")
    print("\t(5) Edgey testing")
    print("\t(6) It's a complex world")
    print("\t(7) Read a custom beginning state from a file\n")

#Args(none)
#Determines the start world based on the player's input, calling the corresponding function.
#Returns(the world selected)
def pickWorld():
    while True:
        choice = input("Selection: ")
        if choice == "1":
            return oneEmpty(SIZE,SIZE)
        elif choice == "2":
            return twoSingleCritter()
        elif choice == "3":
            return threeSingleBirth()
        elif choice == "4":
            return fourthSimpleBirth()
        elif choice == "5":
            return fifthCreateListEdgeCases()
        elif choice == "6":
            return sixthComplexCases()
        elif choice == "7":
            return fileRead()
        else:
            print("Invalid selection! Please try again!")

#args(none)
#asks the user whether they would like to run a turn of the game
#returns(boolean stored in gameRunning)
def runTurn():
    quitOrRun = input("Hit enter to continue (\'q\' to quit): ")
    if quitOrRun in ("q", "Q"):
        return False
    elif quitOrRun == "":
        return True
    elif quitOrRun in ("d","D"):
        debugOn = True
    print("Invalid selection! Please try again!")
    runTurn()
    
#Arguments(int rows, int columns)
#Creates an mxn 2d list of empty cells.
#returns(2d list)
def oneEmpty(rows,columns):
    world = []
    for i in range(rows):
        world.append([])
        for j in range(columns):
            world[i].append(EMPTY)
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @twoSingleCritter()
  @Arguments: None
  @The biosphere is empty except for one location which contains a 
  @Critter.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def twoSingleCritter():
    world = []
    world = [
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @threeSingleBirth()
  @Arguments: None
  @The biosphere is empty except for 3 locations which contain Critters.
  @The 3 Critters are all in proximity to a single location in the 
  @biosphere.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def threeSingleBirth():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " ","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @fourthSimpleBirth()
  @Arguments: None
  @The biosphere contains a number of Critters which are close enough
  @proximity to produce new births for a number of turns.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def fourthSimpleBirth():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", "*","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " ","*", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @fifthCreateListEdgeCases()
  @Arguments: None
  @The biosphere has a Critter located at the edge of the biosphere at
  @each of the 4 compass ponts. Also there is a Critter in each of the
  @corners.
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def fifthCreateListEdgeCases():
    world = []
    world = [
     ["*"," ", "*"," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", "*", " "],
     ["*","*", " "," ", " ", " ", " ", " ", " ", "*"]
    ]
    return(world)

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
"""
  @sixthComplexCases()
  @Arguments: None
  @The biosphere contains a starting pattern that will require a 
  @program to handle births, deaths and edge cases. 
  @Return value: A reference to a 2D list, the initialized biosphere.
"""
def sixthComplexCases():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", "*", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", "*", " ", " ", " ", " "],
     [" "," ", " ","*", "*", "*", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

#args(2d list)
#takes a 2d list and returns the rows and columns that it has. (assumes the list is rectangular)
#returns(int,int)
def findDims(world):
    rows = len(world)
    columns = len(world[0])
    return rows, columns

#args(none)
#prompts the user for a file location, returning an error if invalid, then returns a 2d list 
#containing the information stored in the file.
#returns(2d list)
def fileRead():
    #prompt for a file location and return an error message if it's invalid.
    world = []
    fileOK = False
    while (fileOK == False):
        try:
            filename = input("Name of input file: ")       
            inputfile = open(filename,"r") 
            fileOK = True
            #iterate through all the lines
            currentRow = 0
            aLine = inputfile.readline()
            while (aLine != END_OF_LINE):
                currentCharacter = 0
                world.append([])
                for char in aLine:
                    if char != NEWLINE:
                        world[currentRow].append(char)
                currentRow += 1  
                aLine = inputfile.readline()
            inputfile.close()
        except IOError:
            print("Problem reading from file %s" %(filename))
            fileOK = False
    return world

# Author:  James Tam
# This function was created partially by the above author and is
# used with permission.
# Edits to the function: added support for non-square 2d lists of any size.
# '''
# @display()
# @Argument: two references to the 2D list which is game world.
# @The list must be already created and properly initialized
# @prior to calling this function!
# @Return value: None
# @Displays each element of the world with each row all on one line
# @Each element is bound: above, left, right and below with a bar (to
# @make elements easier to see.
# @Each list is displayed side by side
# <Old list>#<TAB><New list>
# '''
def display(turn,oldWorld,newWorld):
    # Displays a row at a time of each list
    print("Turn #%d" %turn)
    print("BEFORE\t\t\tAFTER")
    rows, columns = findDims(oldWorld)
    for r in range (0,rows,1):

        # Row of dashes before each row of old and new list
        # (Dashes for old list)
        for i in range (0, columns, 1): 
            print("%s" %(" -"), end="")
        print("#\t",end="")
        # (Dashes for new list)
        for i in range (0, columns, 1): 
            print("%s" %(" -"), end="")
        print()

        # Display one row of old world list
        for c in range (0,columns,1):
            # Display: A vertical bar and then element (old list) 
            print("|%s" %(oldWorld[r][c]), end = "")
        # Separate the lists with a number sign and a tab
        print("", end = "#\t")    

        # Display one row of new world list
        for c in range (0,columns,1):
            # Display: A vertical bar and then element (new list) 
            print("|%s" %(newWorld[r][c]), end = "")
        print("|")

    # Row of dashes after end of last row (old world list)
    for i in range (0, columns, 1): 
        print("%s" %(" -"), end="")
    print("#\t",end="")

    # Row of dashes after end of each row (new world list)
    for i in range (0, columns, 1): 
        print("%s" %(" -"), end="")
    print()

#Starting execution point for the program
def start():
    oldWorld = []
    newWorld = []
    gameRunning = True
    turn = 0

    displayStartText()
    newWorld = pickWorld()
    
    while (gameRunning):
        oldWorld, newWorld = updateWorld(newWorld)
        display(turn,oldWorld,newWorld)
        gameRunning = runTurn()
        turn += 1 

    display(turn,oldWorld,newWorld)
start()