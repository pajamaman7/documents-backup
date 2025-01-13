#Thomas Boyko - T08 - 30191728
#poop cleaner, character replacer. v1 - 11/06/22
#Features: generates a 2d list, accepts user input, cleans and searches the list
#based on the input.
#Limitations: clean() and count() could likely have been easily combined into a single function, but
#I elected to keep more to the assignment description.

import random

SIZE = 4
EMPTY = " "
PERSON = "P"
PET = "T"
POOP = "O"
ERROR = "!"
CLEANED = "."
MAX_RANDOM = 10

#args(list,int,int)
#Cleans the 2D list of all entries 'O', replacing with '.'
#returns(output list)
def clean(world,endRow,endColumn):
    print("Scooping the poop")
    outList = world
    #traverses first rows(i), then columns(j)
    i=0
    while (i<=endRow):
        j=0
        while (j<=endColumn):
            if(world[i][j] == POOP):
                outList[i][j] = CLEANED
            j+=1
        i+=1
    return outList

# @args(reference to a alist of characters,integer,integer)
# Function will count the number of occurences of the character specified by the user up the specified
# end point (row/column specified by the user).
# @return(character,integer)
def count(world,endRow,endColumn):
    print("Counting number of occurances of a character")
    number = 0
    i=0
    element = input("Enter character: ")
    #iterates through first the rows(i), then the columns(j) specified.
    while (i<=endRow):
        j=0
        while (j<=endColumn):
            if (world[i][j] == element):
                number+=1  
            j+=1
        i+=1 
    print("# occurances of %s=%d" %(element,number))
    return(element,number)


# Randomly generates an 'occupant' for a location in the world
# @args(none)
# Randomly generates and returns a character according to the specified probabilities.
#  *50% probability empty space
#  *20% probability of a person
#  *10% probability of a pet
#  *20% probability of fecal matter
# @return(character)
def createElement():
    tempNum = random.randrange(MAX_RANDOM)+1

    # 50% chance empty
    if ((tempNum >= 1) and (tempNum <= 5)):
        tempElement = EMPTY 

    # 20% of a person
    elif ((tempNum >= 6) and (tempNum <= 7)):
        tempElement = PERSON

    # 10% chance of pet
    elif (tempNum == 8):
        tempElement = PET

    # 20% chance of poop in that location (lots in this world)
    elif ((tempNum >= 9) and (tempNum <= 10)):
        tempElement = POOP

    # In case there's a bug in the random number genrator
    else:
        tempElement = ERROR

    return(tempElement)

# Creates the SIZExSIZE world. Randomly populates it with the 
# return values from function createElement
# @args(none)
# Randomly populates the 2D list which is returned to the caller.
# @return(reference to a list of characters)
def createWorld():
    world = [] #  Create a variable that refers to a 1D list. 
    r = 0

    #  Outer 'r' loop traverses the rows. 
    # Each iteration of the outer loop creates a new 1D list.
    while (r < SIZE):
        tempRow = []  
        world.append(tempRow)  # Create new empty row
        c = 0
        # The inner 'c' loop traverses the columns of the newly 
        # created 1D list creating and initializing each element
        # to the value returned by createElement()
        while (c < SIZE):
            element = createElement()
            tempRow.append(element)
            c = c + 1
        r = r + 1    
    return(world)

# Shows the elements of the world. All the elements in a row will
# appear on the same line.
# @args(reference to a list of characters)
# Displays the 2D list with each row on a separate line.
# @return(nothing)
def display(world):
    print("OUR WORLD")
    print("========")
    r = 0
    while (r < SIZE): # Each iteration accesses a single row 
        c = 0
        while (c < SIZE):  # Each iteration accesses an element in a row
            print(world[r][c], end="")
            c = c + 1
        print()  # Done displaying row, move output to the next line
        r = r + 1 

# @args(none)
# Gets user input to determine how much of the world list should be searched.
# @return(integer,integer)
def getEndPoint():
    #Declaring local variables
    endRow = -1
    endColumn = -1
    #get user input, using two loops, one for row and one for column.
    #the if statements inside check for values outside the specified range,
    #or for any input of the wrong type; ie letters or floats.
    while (endRow<0 or endRow>3):
        endRow = int(input("Enter end row for operation (0-3): "))
        if (endRow<0 or endRow>3 or type(endRow)!=int):
            print("Error: You entered %d"%endRow)
            print("Error: Enter a value between 0 and 3")
    while (endColumn<0 or endColumn>3):
        endColumn = int(input("Enter end column for operation (0-3): "))
        if(endColumn<0 or endColumn>3 or type(endColumn)!=int):
            print("Error: You entered %d"%endColumn)
            print("Error: Enter a value between 0 and 3")
    return(endRow,endColumn)


# Starting execution point for the program.
def start():
    world = createWorld()
    display(world)
    endRow,endColumn = getEndPoint()
    element,number = count(world,endRow,endColumn)
    world = clean(world,endRow,endColumn)    
    display(world)

start()