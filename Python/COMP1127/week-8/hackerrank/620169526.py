def leapYear(year):
#  a leap year occurs if the year is divisible by 4 but not 100
#  it also occurs if it is divisible by 400
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def closestLeapYear(year):
  
  
  if leapYear(year):
    return year

  futureYear = year + 1 
  pastYear = year - 1  

  #  search until we find the closest leap year 
  while True:

    #  if both a past and future leap year are found
    #  just return the one closest to the given year 
    if leapYear(pastYear) and leapYear(futureYear):
        # this should choose the one closer in absolute difference frl 
        return pastYear if year - pastYear <= futureYear - year else futureYear  
    elif leapYear(pastYear):
        return pastYear
    elif leapYear(futureYear):
        return futureYear

    # if at the end of the search no leap year is found yet
    #  just move one year further in both the past and the future 
    pastYear -= 1
    futureYear += 1
      
def findLastLeapYears(yearBounds):
  
    if not yearBounds:
      return []
    
    return [closestLeapYear(year) for year in yearBounds]
  
  
print(findLastLeapYears([1995, 1750, 2018]))


  