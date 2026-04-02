from datetime import date

CURRENTDATE = date.today()

def future_date(year, month, day):
  
  enteredDate = date(year, month, day)
  
  return True if enteredDate >  CURRENTDATE else False


print(future_date(2020, 9, 23))
  
  
  
