OBJECT = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def zellerCongruence(year, month, day):
  
    if month == 1 or month == 2:
      month += 12
      year -= 1
    
    return (day + (13 * (month + 1)) // 5 + year + year // 4 - year // 100 + year // 400) % 7


def weekDay(year, month, day):
  
  result = int(zellerCongruence(year, month, day))
  
  return OBJECT[(result + 5) %7]


# print(weekDay(2010,5,9))