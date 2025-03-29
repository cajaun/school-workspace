from question1 import get_courses,computeLetterGrade,student

def calcLetterGrade(std):
    courses = get_courses(std)
    course_grades = []

    for course, grade in courses:
    
        letter_grade = computeLetterGrade(grade)
 
        course_grades.append((course, letter_grade))
    return course_grades

student_instance = student("620000101", "Jane", "Doe",[
    "COMP1126", 80,
    "COMP1127", 60,
    "COMP1210", 50,
    "COMP1161", 60,
    "COCR2003", 85,
    "COMP2140", 80
])

print(calcLetterGrade(student_instance))