def pred(n):
  return n - 1


def succ(n):
  return n + 1

def addition(x, y):
  
  if y == 0:
    return x
  else:
    return addition(succ(x), pred(y))
  
print(addition(5,3))


def subtraction(x,y):
  
  if y == 0:
    return x
  else:
    return subtraction(pred(x), pred(y))
  
print(subtraction(5,3))