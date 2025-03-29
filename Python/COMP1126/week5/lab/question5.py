from question3 import sumDigits
from question4 import skip_power
import sys

sys.setrecursionlimit(999999999)


def skip_valid_power(x,y):
  res = skip_power(x,y)
  
  if 1000 <= res <= 999999:
    if(sumDigits(res) % 7 == 0):
      return True
  return False
  
print(skip_valid_power(10,4))
print(skip_valid_power(12,6))