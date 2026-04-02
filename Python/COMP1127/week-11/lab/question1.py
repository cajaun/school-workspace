def my_map(f,lst):
    if lst == []:
        return []
    else:
        return [f(lst[0])] + my_map(f, lst[1:])

def myzip(lst1,lst2):
    if lst1 ==[] or lst2 == []:
        return []
    else:
        return [(lst1[0],lst2[0])] + myzip(lst1[1:],lst2[1:])

def student(sid,fname,lname, crses):
    """Constructor for student"""
    courses = []
    while crses != []:
        courses += [(crses[0],crses[1])]
        crses = crses[2:]
    return [sid,[fname,lname],courses]

def get_id(std):
    """Returns students ID"""
    return std[0]

def get_name(std):
    """Returns students Name"""
    return std[1]

def get_courses(std):
    """Returns a list of tuples of course codes and grade"""
    return std[2]

def get_fname(name):
    """Returns first name"""
    return name[0]

def get_lname(name):
    """Returns last name"""
    return name[1]

def get_ccode(course_det):
    """Returns course code part of the tuple"""
    return course_det[0]

def get_grade(course_det):
    """Returns grade part of the tuple"""
    return course_det[1]

def calc_gpa(std):
    courses = get_courses(std)
    total_quality_points = 0
    total_credits = 0

    for course, grade in courses:
        letter_grade = computeLetterGrade(grade)
        quality_points = qp_list[letter_grade]
        credits = credit_list[course]
        

        total_quality_points += quality_points * credits
        total_credits += credits

    gpa = total_quality_points / total_credits if total_credits > 0 else 0
    return gpa
    
       
## For this function to work you first need to write calc_gpa()
def print_students_gpa(std):
    """Prints the student's details and GPA to the console"""
    print("Student Id:", get_id(std))
    print("Student Name:", get_fname(get_name(std)), get_lname(get_name(std)))
    print("GPA: {:.2f}".format(calc_gpa(std)))



def computeLetterGrade(num_grade):
    grade_mapping = {
        range(90, 101): "A+",
        range(80, 90): "A",
        range(75, 80): "A-",
        range(70, 75): "B+",
        range(65, 70): "B",
        range(60, 65): "B-",
        range(55, 60): "C+",
        range(50, 55): "C",
        range(45, 50): "F1",
        range(40, 45): "F2",
        range(0, 40): "F3"
    }
    
    for grade_range, letter in grade_mapping.items():
        if num_grade in grade_range:
            return letter
    return "Invalid Grade"

credit_list={'COMP1126':3,'COMP1127':3,'COMP1161':3,'COMP1210':3,'COMP1220':3,'COMP2140':3,\
                 'COMP2111':3,'COCR2003':1}

qp_list = {"A+":4.3,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"F1":1.7,"F2":1.3,\
               "F3": 0.0}

# print(computeLetterGrade(80))





