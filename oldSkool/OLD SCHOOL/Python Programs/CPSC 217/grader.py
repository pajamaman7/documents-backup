#Thomas Boyko 
#ID: 30191728 
#Tutorial T08
#GPA Calculator v1.0 - for the described marking system in CPSC 217
#Calculator only allows for numeric inputs
#Sept. 19 2022

#Create constants for exam and assignment weighting:
WEIGHT_A1 = .15
WEIGHT_A2 = .15
WEIGHT_A3 = .2
WEIGHT_MIDTERM = .2
WEIGHT_FINAL = .30

#Requesting user input strings, converting to float:
print("Entering grades for assignments")
grade_a1 = float(input("\nA1 grade point (0.0-4.0): "))
grade_a2 = float(input("A2 grade point (0.0-4.0): "))
grade_a3 = float(input("A3 grade point (0.0-4.0): "))
print("\nEntering grades for examinations")
grade_midterm_exam = float(input("\nMidterm exam grade point (0.0-4.3): "))
grade_final_exam = float(input("Final exam grade point (0.0-4.3): "))

#Calculate weighted assignments & exams
weighted_assignment = (WEIGHT_A1*grade_a1 +
                       WEIGHT_A2*grade_a2 +
                       WEIGHT_A3*grade_a3)
weighted_exams =      (WEIGHT_MIDTERM*grade_midterm_exam+
                       WEIGHT_FINAL*grade_final_exam)
final_mark = weighted_assignment + weighted_exams

#display the user input in proper format
print("\nOriginal and weighted grade points, term grade point")
print('%27s\t%.1f\t%.1f\t%.1f' % ("Assignments:", grade_a1, grade_a2, grade_a3))
print('%27s\t%.1f\t%.1f' % ('Examinations:', grade_midterm_exam, grade_final_exam))
print('%27s\t%.1f\t%.1f' % ('Weighted assignments/exams:', weighted_assignment, weighted_exams))
print('%27s\t%.1f' % ('Final mark:', final_mark))