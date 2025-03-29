def div(x,y):
  
  if x < y:
    return 0
  else:
    return 1 + div(x - y, y)
  
# print(div(18,4))


def mod(x,y):
  
  if x < y:
    return x
  else:
    return mod(x - y, y)
  
# print(mod(18,4))

