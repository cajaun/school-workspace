# Question 2

def barstool(number):
  
  if (( number % 3 == 0) and (number % 7 == 0)) :
    return "BarStool"
  elif (number % 7 == 0):
    return "Stool"
  elif (number % 3 == 0):
    return "Bar"
  else:
    return "No Bar No Stool"
  
  
print(barstool(15))
print(barstool(14))
print(barstool(21))
print(barstool(25))