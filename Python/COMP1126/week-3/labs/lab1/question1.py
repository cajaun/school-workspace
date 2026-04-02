# Question 1

from datetime import date

CURRENTDATE = date.today()

def time_existed(dayOfBirth, monthOfBirth, yearOfBirth, name):

  dateOfBirth = date(yearOfBirth, monthOfBirth, dayOfBirth)
  days = (CURRENTDATE - dateOfBirth).days
  
  return f"{name} has lived for {days} days"
  

name = input("What is your name: ")
dayOfBirth = int(input("What day were you born on: "))
monthOfBirth = int(input("What month were you born in: "))
yearOfBirth = int(input("What year were you born in: "))

print(time_existed(dayOfBirth, monthOfBirth, yearOfBirth, name))