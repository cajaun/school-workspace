LENGTH = 0
GRADES = [None] * LENGTH

def gradePrompt():
  
  LENGTH = int(input("How many grades are there: "))
  for i in range(LENGTH):
    GRADES[i] = int(input("Enter a grade: "))
  
  return GRADES
    
    
gradePrompt()
print(GRADES)
    
    
    
  
  