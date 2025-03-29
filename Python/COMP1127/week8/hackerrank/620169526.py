def leapYear(year):
 
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def closestLeapYear(year):
  
  
  if leapYear(year):
    return year

  futureYear = year + 1 
  pastYear = year - 1  

  while True:

    if leapYear(pastYear) and leapYear(futureYear):
     
        return pastYear if year - pastYear <= futureYear - year else futureYear
    elif leapYear(pastYear):
        return pastYear
    elif leapYear(futureYear):
        return futureYear


    pastYear -= 1
    futureYear += 1
      
def findLastLeapYears(yearBounds):
  
    if not yearBounds:
      return []
    
    return [closestLeapYear(year) for year in yearBounds]
  
  
print(findLastLeapYears([1900, 1600, 1581, 1995, 1750, 2016]))


  