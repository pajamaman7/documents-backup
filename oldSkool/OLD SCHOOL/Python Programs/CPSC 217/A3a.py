#Thomas Boyko - T08 - 30191728
#find and replace program v1 11/06/22
#features: generates a random list, asking the user to input a character to 
#be found, and another to be replaced.
#limitations: only a select set of ascii characters can be used in the program;
#however, any character in the input list can be changed in the output list

import random

MAX_ELEMENTS = 25

# Each character is assigned a numeric (ASCII) code e.g. A = 65, B = 66
# a = 97, b = 98... { = 123...
# For the extended code set: https://www.ascii-code.com/
MIN_CHAR = 33
MAX_CHAR = 126

# args(none)
# return(a randomly generated character) from ! to ~
def generateElement():
    #Declare variables for function
    aChar = " "
    dieRoll = -1

    dieRoll = random.randrange(MIN_CHAR,(MAX_CHAR+1))
    aChar = chr(dieRoll)     # Function to convert ASCII code to a character
    return (aChar)

# args(none)
# Creates a list of 1 - 100 elements each element a string of length 1
# return (reference to the list)
def createList():
    #Declare variables for function
    aList = []
    size = -1
    i = -1

    size = random.randrange(1,(MAX_ELEMENTS+1))
    i = 0
    while (i < size):
        aList.append(generateElement())        
        i = i + 1    
    return(aList,size)

# args(list to be printed, size of said list)
# displays an index followed by each list element on it's own line
# return(nothing)
def display(aList,size):
    #Declare variables for function
    i = 0
    while (i < size):
        print("Element at index[%d]=%s" %(i,aList[i]))
        i = i + 1    

#args(none)
#prompts the user for two characters
#returns(the two characters)
def getFindAndReplaceCharacters():
    find = input("Please input a character to be replaced: ")
    replace = input("Please input a character it will be replaced with: ")
    return find, replace

#args(char(string),char(string),list,int)
#Takes a list, a letter to find, and one to replace, and replaces all instances
#of the find letter with the replace letter. I was able to use a for loop to avoid using the size 
#variable.
#returns (list)
def findAndReplace(find, replace, aList, size):
    outputList = []
    for letter in aList :
        if (letter == find):
            outputList.append(replace)
        else:
            outputList.append(letter)
    return outputList


#Starting execution point for the program
def start():
    #Declare variables local to start
    aList = []
    size = -1

    aList,size = createList()
    display(aList,size)
    find, replace = getFindAndReplaceCharacters()   
    outputList = findAndReplace(find, replace,aList,size)
    display(outputList,size)

start()
