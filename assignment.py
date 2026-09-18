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


#calculating grade based on the three averages 
def calculate_grade(assignment_average, quiz_average, test_average):
    assignment_portion = assignment_average * 0.30
    quiz_portion = quiz_average * .30
    test_portion = test_average * .40
    overall_grade = assignment_portion + quiz_portion + test_portion
    return overall_grade

overall_grade = calculate_grade(assignment_average, quiz_average, test_average)
print()
print("Overall Grade:", overall_grade)

# determining letter grade 
def letter_grade(overall_grade): 
    if overall_grade >= 90: 
        grade = "A"
    elif overall_grade >= 80: 
        grade = "B"
    elif overall_grade >= 70: 
        grade = "C"
    elif overall_grade >= 60: 
        grade = "D"
    else: 
        grade = "F"
    return grade 

letter_grade = letter_grade(overall_grade)
print("Letter Grade:", letter_grade)

# determining attendance status 
def attendance_status(attendance): 
    if attendance >= 95: 
        presence = "Excellent Attendance"
    elif attendance >= 90: 
        presence = "Good Attendance"
    elif attendance >= 80: 
        presence = "Attendance Warning"
    else: 
        presence = "Poor Atendance"
    return presence

attendance = attendance_status(attendance_percentage)
print("Attendance Status:", attendance)

# deterniming if there any missing assignments, and outputing status
def assignment_status(missing_assignments): 
    if missing_assignments == 0: 
        warning = "Excellent"
    elif missing_assignments >= 5: 
        warning = "Critical"
    elif missing_assignments >= 3: 
        warning = "Warning"
    elif missing_assignments >= 1:
        warning = "Good"
    return warning 


# determining if they pass all three requirements 
def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70: 
        if attendance >= 90: 
            if missing_assignments <= 2: 
                print("Academic Eligibility: ELIGIBLE")
                print("Reason: Student passed all three requirements.")
            else: 
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments.")
        else:
            print("Academic Eligibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low.")
    else: 
        print("Academic Eligibility: NOT ELIGIBLE")
        print("Reason: Overall grade is too low.")


# detereming if student has high honors 
def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90: 
        if attendance >= 95: 
            if missing_assignments == 0: 
                print("High Honors: YES")
            else: 
                print("High Honors: NO")
                print("Reason: Student has missing assignments.")
        else:
            print("High Honors: NO")
            print("Reason: Attendance requirement not met.")
    else: 
        print("High Honors: NO")
        print("Reason: Grade requirement not met.")


# determing if student has good standing 
def check_good_standing(overall_grade, attendance):
    if (overall_grade >= 70) and (attendance >= 90): 
        print("Good Standing: YES")
    else: 
        print("Good Standing: NO")


# determining if student needs support 
def check_support(overall_grade, attendance):
    if (overall_grade < 70) or (attendance < 80): 
        print("dditional Support: RECOMMENDED")
    else: 
        print("Additional Support: NOT NEEDED")


print() 
print() 

# checking if login is correct 
user_name = input("Enter username: ")

if (user_name == "student"): 
    pin = int(input("Enter PIN: "))
    if (pin == 1234): 
        print("Login Successful!")
    else: 
        print("Login Failed: Incorrect PIN.")
else: 
    print("Login Failed: Incorrect username.")


# giving a message depending on student's grade 
def grade_level_message(grade_level):
    if grade_level == 12: 
        print("Senior year - finish strong!")
    elif grade_level == 11: 
        print("Junior year - keep pushing!")
    elif grade_level == 10: 
        print("Keep builing your skills!")
    elif grade_level == 9: 
        print("Welcome to freshman year!")
    else: 
        print("Invalid grade level")



# showing what the student's strongest category
def strongest_category(assignment_average, quiz_average, test_average):
    if assignment_average > quiz_average: 
        if assignment_average > test_average: 
            print("Strongest Category: Assignments")
        else: 
            print("Strongest Category: Tests")
    else: 
        if quiz_average > test_average: 
            print("Strongest Category: Quizzes")
        else: 
            print("Strongest Category: Tests")


# extra credit 
def check_advanced_status(overall_grade, attendance, missing_assignments): 
    if (overall_grade >= 90 and attendance >= 95) or (overall_grade >= 85 and missing_assignments == 0):
        print("Advanced Status: OUTSTANDING STUDENT")
    else: 
        print("Advanced Status: STANDARD STUDENT STATUS")



print()
print() 
print("-----------------------------------")
print("          STUDENT SUMMARY          ")
print("-----------------------------------")

print("Student:", student_name)
print("Grade Level:", grade_level)

print() 
print() 

print("Assignment Average:", assignment_average)
print("Quiz Average:", quiz_average)
print("Test Average:", test_average)

print()
print()

print("Overall Grade:", overall_grade)
print("Attendance:", attendance)
print("Missing Assignments:", missing_assignments)
print("Missing Assignment Status:", assignment_status(missing_assignments))

print()
print() 

check_eligibility(overall_grade, attendance_percentage, missing_assignments)
print()
check_high_honors(overall_grade, attendance, missing_assignments)
print()
check_good_standing(overall_grade, attendance_percentage)
print()
check_support(overall_grade, attendance_percentage)
print()
grade_level_message(grade_level)
print()
strongest_category(assignment_average, quiz_average, test_average)
print()
check_advanced_status(overall_grade, attendance_percentage, missing_assignments)
print()
print()