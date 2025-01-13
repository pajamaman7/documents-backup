#Thomas Boyko
#GPA Converter to letter grades
#Calculator only allows for numeric inputs, wll prompt user again if an invalid number is submitted
#Sept. 19 2022
#301917280
#Tutorial T08

#Define constants for input contsraints and grade cutoffs
GRADE_MIN = 0
GRADE_MAX = 4.3

CUTOFF_APLUS = 4.06
CUTOFF_A = 3.85
CUTOFF_AMINUS = 3.5
CUTOFF_BPLUS = 3.15
CUTOFF_B = 2.85
CUTOFF_BMINUS = 2.5
CUTOFF_CPLUS = 2.15
CUTOFF_C = 1.85
CUTOFF_CMINUS = 1.5
CUTOFF_DPLUS = 1.15
CUTOFF_D = 0.85
CUTOFF_F = 0.0

numGrade = -1

#check for valid input and prompt user again if an invalid input is presented
while (numGrade<0 or numGrade>4.3):
    numGrade = float(input("Term grade point (0-4.3): "))

#if and elif chain to map each grade to a letter
if (numGrade==CUTOFF_APLUS):
    letterGrade = "A+"
elif (numGrade>=CUTOFF_A):
    letterGrade = "A"
elif (numGrade>=CUTOFF_AMINUS):
    letterGrade = "A-"
elif (numGrade>=CUTOFF_BPLUS):
    letterGrade = "B+"
elif (numGrade>=CUTOFF_B):
    letterGrade = "B"
elif (numGrade>=CUTOFF_BMINUS):
    letterGrade = "B-"
elif (numGrade>=CUTOFF_CPLUS):
    letterGrade = "C+"
elif (numGrade>=CUTOFF_C):
    letterGrade = "C"
elif (numGrade>=CUTOFF_CMINUS):
    letterGrade = "C-"
elif (numGrade>=CUTOFF_DPLUS):
    letterGrade = "D+"
elif (numGrade>=CUTOFF_D):
    letterGrade = "D"
elif (numGrade>=CUTOFF_F):
    letterGrade = "F"
#print numGrade and letter grade with correct formatting
print("Term GPA: %.1f \t Term letter: %s" % (numGrade, letterGrade))
