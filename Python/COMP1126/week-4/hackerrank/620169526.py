# ID Number: 620169526

# Hackerrank Handle: valmiera

# Hackerrank Exercise: Standard Deviation 1

# Code submission from Hackerrank: 

import math 

def standardDeviation(*args):
  
  array = list(args)
  total = 0
  
  for number in range(len(array)):
    total += array[number]
    
  average = total / len(array)
  
  newArray = [ round((number - average), 2) ** 2 for number in array]
  
  squareTotal= sum(newArray)
  
  standardDeviation = round(math.sqrt((squareTotal/10)), 3)
  
  return standardDeviation
  
    

print(standardDeviation(10,4,7,9,4,6,8,1,9,8))
    
  
  
  