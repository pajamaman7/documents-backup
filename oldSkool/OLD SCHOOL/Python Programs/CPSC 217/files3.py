#Thomas Boyko - T08 - 30191728
#File reader v1 11/21/22
#Program will prompt the user for the name of a file, then read the data in said file and display
#it back, summing the numbers in each line.

#Define constants
END_OF_LINE = ""
EMPTY = ""
NEWLINE = "\n"
SPACE = " "
TAB = "\t"

#File reading component of the program
#args(none)
#returns(2D list)
def fileRead():
    #prompt for a file location and return an error message if it's invalid.
    jobNums = []
    fileOK = False
    while (fileOK == False):
        try:
            filename = input("Name of input file: ")       
            inputfile = open(filename,"r") 
            fileOK = True
            #this will read the first line, ignoring it, as there's no helpful information in it.
            aLine = inputfile.readline()
            if (aLine == EMPTY):
                print("%s is an empty file")
            else:
                aLine = inputfile.readline()
                currentRow = 0
                while (aLine != END_OF_LINE):
                    currentCharacter = 0
                    jobNums.append([])
                    while (aLine[currentCharacter] not in (TAB, NEWLINE)):
                        #Only add nums not spaces to the list of numbers
                        if (aLine[currentCharacter] != SPACE):
                            jobNums[currentRow].append(int(aLine[currentCharacter]))
                        currentCharacter += 1
                    currentRow += 1  
                    aLine = inputfile.readline()                                                 
                inputfile.close()
        #adding valueError here throws an error message if the file contains any characters that can't be converted to int
        except (IOError, ValueError):
            print("Problem reading from file %s" %(filename))
            fileOK = False
    return jobNums
    
#Display component of the program
#args(2D list)
#returns(none)
def display(listIn):
    rowNumber = 0
    while rowNumber < len(listIn):
        aLine = ""
        rowTotal = 0
        for column in listIn[rowNumber]:
            aLine += "%s-"%column
            rowTotal += column
        aLine += "Total=%d"%rowTotal
        print(aLine)
        rowNumber += 1 

#Starting execution point for the program
def start():
    display(fileRead())
    
start()