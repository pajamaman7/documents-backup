
exams = 2.0
assignments = 4.0
EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.5


weightedExam = (exams * EXAM_WEIGHT)
weightedAssignment = (assignments * ASSIGNMENT_WEIGHT)
termGPA = weightedExam + \
          weightedAssignment #Multiple lines used only for learning purposes
print("Exam GPA: %4.1f\tAssignment GPA%4.1f" \
      %(exams,assignments))
print("Weighted exam GPA: %4.1f\tWeighted assignment GPA%4.1f" \
      %(weightedExam,weightedAssignment))
print("Term GPA %4.2f" %(termGPA))
