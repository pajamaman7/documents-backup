#Changes: put the euclid part 2 string addition into the combination function.


import math

gcdwork = "$\n \\begin{array}{lcl}"
AMP = " & "
NEWLINE = " \n "
TIMES = " \\times "
PLUS = " + "
EQUALS = "="

def linIntComb (a, b, n):
    global euc2
    # traverse for all possible values
    i = 0
    while i * a <= n:
         
        # check if it is satisfying
        # the equation
        if (n - (i * a)) % b == 0:
            
            # add to the second step of the string
            # format: 2023 & 1 & 0
            #         greater & a & b
            x,y = i, int((n-(i*a)/b))
            euc2 = NEWLINE + str(n) + AMP + str(x) + AMP + str(y) + "\\\\" + euc2
            return x,y
        i = i + 1
    

def gcd(greater, lesser):
    global gcdwork,euc2
    if(greater<lesser):
        greater,lesser = lesser,greater
    if ( lesser==0 ):
        print("The greatest common denominator is: " + str(greater))
        gcdwork += NEWLINE + "\\end{array} \n$"
        euc2 = "$ \n \\begin{array}{lcl}" + euc2
        return greater
    #formula : a = bq+r
    #greater = lesser*q + r
    q = math.floor(greater/lesser)
    r = greater - lesser*q
    # add to the string for the first step
    gcdwork = gcdwork + NEWLINE + str(greater) + AMP + EQUALS + AMP + str(lesser) \
        +TIMES + str(q) + PLUS + str(r) + "\\\\"

    x,y = linIntComb(int1,int2,greater)

    return gcd(lesser,r)

def getUserInput():
    num1 = input("Enter the first of the two numbers you'd like to take gcd() of: ") 
    num2 = input("Enter the second of the two numbers you'd like to take gcd() of: ")
    return int(num1),int(num2)

def main():
    global int1
    global int2
    global euc2
    euc2 = "\n \\end{array} \n$"
    print(linIntComb(-1,2,3))
    greater, lesser = getUserInput()
    int1,int2 = greater, lesser
    linIntComb(int1,int1,int2)
    linIntComb(int2,int1,int2)
    gcd(greater, lesser)
    print(euc2)

main()