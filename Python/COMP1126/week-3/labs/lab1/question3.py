# Question 3

REMAINDERTWO = "FIFA Men World Cup"
REMAINDERTHREE = "ICC Cricket World Cup, FIFA Women World Cup and Netball World Cup"
LEAPYEAR = "Olympics, Copa America and European Championship"
NOTREMAINDERTWOORTHREE = "IAAF World Athletic Championships and Gold Cup"


def leapCalc(year):
  
  if ((year % 4 == 0 and year % 100 != 0 ) or ( year % 100 == 0 and year % 400 == 0) ):
    return True
  return year % 4


def majorSportYear(year):
  
  remainder = leapCalc(year)
  
  if remainder is True:
    return LEAPYEAR
  elif remainder == 2:
    return REMAINDERTWO
  elif remainder == 3:
    return REMAINDERTHREE
  else:
    return NOTREMAINDERTWOORTHREE

print(majorSportYear(2000))
print(majorSportYear(2001))
print(majorSportYear(2002))