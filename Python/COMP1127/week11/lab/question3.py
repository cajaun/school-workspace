from question1 import credit_list, qp_list, student, print_students_gpa


def convertToWtqp(c_pair):
    course_code, letter_grade = c_pair
    credit = credit_list[course_code] 
    quality_points = qp_list[letter_grade]  
    
    return (credit, quality_points)

student_instance = student("620000101", "Jane", "Doe", [
    "COMP1126", 80,
    "COMP1127", 60,
    "COMP1210", 50,
    "COMP1161", 60,
    "COCR2003", 85,
    "COMP2140", 80
])

print_students_gpa(student_instance)