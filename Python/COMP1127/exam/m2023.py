def isMultiple(a,b):
  
  return a % b == 0 


def multipleList(a,b):
  

  return  [i for i in range(a, b + 1) if isMultiple(b,i)]


res = multipleList(28, 7)
print(multipleList(28, 7 ))


def tripleSumList(lst):
  
  return sum([num*3 for num in lst])

print(tripleSumList(res))

def prefectOrNot(a,b):
  
  ml = multipleList(a,b)
  res = tripleSumList(ml)
  if res % 12 == 0:
    return "Perfect Triple Pair"
  else:
    return "Not Perfect Triple Pair"
  
  
print(prefectOrNot(2,30))

# print(prefectOrNot(2,30))
  
# Define the make_student function
# Assume it creates a student record as a tuple with a tag "student"
def make_student(student_id, name, dob, courses):
    return ("student", [student_id, name, dob, courses])

# Define the add_student function
def add_student(student, student_list):
    student_list.append(student)

# Function to add a course to a student
def add_course(sid, ccode, cgrade, clgrade, slst):
    for tag, student in slst:
        if tag == "student" and student[0] == sid:  # Access student_id from the tuple
            student[3].append((ccode, cgrade))  # Access courses from the student list
            print(f"Student {sid} attained grade {clgrade}.")
            return
    print(f"Student {sid} not found in the list.")

# foldr implementation
def foldr(combiner, base, lst):
    if lst == []:
        return base
    else:
        return combiner(lst[0], foldr(combiner, base, lst[1:]))

# Function to calculate the total number of grades
def tot_number_grades(slst):
    return foldr(lambda x, y: x + y, 0, [len(student[3]) for tag, student in slst if tag == "student"])

# Function to calculate the overall average
def overallAverage(slst):
    total_grades = foldr(lambda x, y: x + y, 0, [sum(course[1] for course in student[3]) for tag, student in slst if tag == "student"])
    total_number_of_courses = foldr(lambda x, y: x + y, 0, [len(student[3]) for tag, student in slst if tag == "student"])
    return total_grades / total_number_of_courses if total_number_of_courses > 0 else 0

# Example Usage
student_list = []
st1 = make_student(1001, ["Jane", "Doe"], (1995, 12, 25), [("COMP1126", 83), ("COMP1127", 92), ("COMP1210", 77)])
st2 = make_student(1002, ["Joe", "White"], (2000, 4, 20), [("COMP1120", 66)])

add_student(st1, student_list)
add_student(st2, student_list)

# Add a course to a student
add_course(1002, "COMP1126", 91, "A+", student_list)

# Total number of grades
total_grades = tot_number_grades(student_list)
# print("Total number of grades:", total_grades)

# Overall average
overall_avg = overallAverage(student_list)
# print("Overall average grade:", overall_avg)


def makeIncidentReport(address, town, incidentType):
  
  return [address, town, incidentType]

# def getIncidentPriorityValue(r):
  
  
# lst= [2 , 6 , 10 , 4 , 12]
# lst2 = lst. sort( )
# print(lst) 