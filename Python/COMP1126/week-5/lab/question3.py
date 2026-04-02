from question2 import mod, div
# import sys

# sys.setrecursionlimit(99999999)

def lastDigit(x):
  return mod(x, 10)

def allButLast(x):
  return div(x, 10)

def sumDigits(x):
  
  if x < 10:
    return x
  else:
    return sumDigits(allButLast(x)) + lastDigit(x)
  
print(sumDigits(234))