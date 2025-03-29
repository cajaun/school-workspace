from extra_file import *

def cube_numberV1(n):
  cube = n * n * n
  print(cube)
  
  
  
def cube_numberV2(n):
  cube = n * n * n
  return cube


def mystery(num):
  #This function takes a number as input and triples it and adds 9 to it
  num=num*3
  newnum=num + 25
  return newnum