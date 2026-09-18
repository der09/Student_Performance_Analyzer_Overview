# Name: Diane Hsieh 
# Period: AM 
# Student Performance Analyzer 

print() 
# Program Introduction 

print("===============================")
print(" STUDENT PERFORMANCE ANALYZER ")
print("===============================")

#student information
student_name = input("What is the student's name?: ")
grade_level = float(input("What grade level is the student in?: "))
assignment_average = float(input("What is the student's assignment average?: "))
quiz_average = float(input("What is the student's quiz average?: "))
test_average = float(input("What is the student's test average?: "))
attendance_percentage = float(input("What is the student's attendance percentage?: "))
missing_assignments = int(input("How many missing assignments does the student have?: "))

def calculate_grade(assignment_average, quiz_average, test_average):
    assignment_portion = assignment_average * 0.30
    quiz_portion = quiz_average * .30
    test_portion = test_average * .40
    overall_grade = assignment_portion + quiz_portion + test_portion
    return overall_grade

print("Overall grade:, calculate_grade(assignment_average, quiz_average, test_average)")

def letter_grade(overall_grade): 
    