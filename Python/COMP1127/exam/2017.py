def isMultiple(a,b):
  
  return a %b == 0


def multipleList(a,b):
  
  return [x for x in range(b, a + 1) if isMultiple(x, b)]


def triple(lst):
  
  return sum([x*3 for x in lst if x != lst[0] and x != lst[-1]])

res = triple(multipleList(14,2))
print(res)