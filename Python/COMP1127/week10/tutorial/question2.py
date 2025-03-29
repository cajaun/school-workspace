def makeStack():
  return ("stack", [])


def contents(stk):
  return stk[1]


def isStack(obj):
  
  return obj[0] == "stack" and isinstance(obj, tuple) and isinstance(obj[1], list)


def push(stk, el):
  if isStack(stk):
    contents().append(el)
    
def top(stk):
  
  if not isStackEmpty(stk):
    stk[1][0]
    
def pop(stk):
  
  if not isStackEmpty(stk):
    stk[1].pop(0)
    
    
def isStackEmpty(stk):
  
  return len(stk) == 0