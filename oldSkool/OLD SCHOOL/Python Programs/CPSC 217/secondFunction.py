#Thomas Boyko - 30191728 - T08
#Second function program - v1 10/17/22
#Features - input function, doubling function, output function, main function
#Capable of handling inputs that are not convertable to float.

def getInput():
    while True:
        try:
            userInput = float(input("Enter a number to be doubled: "))
            break
        except:
            print("Oops! That's not a number!")
    return userInput 

def doubleIt(num):
    return num * 2

def display(doubledNum):
    print("Your number times two: %.2f"%(doubledNum))

def start():
    userNum = getInput()
    doubledUserNum = doubleIt(userNum)
    display(doubledUserNum)
start()
