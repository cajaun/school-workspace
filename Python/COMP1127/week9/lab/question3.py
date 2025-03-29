from question2 import weekDay

def unlucky(year):
  
  return [(13, month, year) for month in range(1,13) if weekDay(year,month, 13 ) == "Friday"]

print(unlucky(2010))
# print(unlucky(2009))