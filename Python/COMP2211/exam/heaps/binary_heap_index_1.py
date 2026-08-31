# heap for index 1

def isEmpty(vec, i):
  return i > vec[0]

def isLeaf(vec, i):
  return 2 * i > vec[0] and i <= vec[0]

def left(i):
  return 2 * i

def right(i):
  return 2 * i + 1

def parent(i):
  return i // 2

def bubbleUp(vec, i):
  
  while i > 1 and vec [i] < vec[parent(i)]:
    vec[i] = vec[parent(i)]
    vec[parent(i)] = vec[i]
    i = parent(i)
    
def insert(vec, value):
  size = vec[0]
  posn = size + 1
  vec[posn] = value
  vec[0] = size + 1
  bubbleUp(vec, posn)
    
def search(vec, i, value):
    size = vec[0]
    
    if i > size:
      return False
    
    if vec[i] == value:
      return True
    
    if value < vec[i]:
      return False
    
    return search(vec, 2 * i, value) or search(vec, 2 * i + 1, value)

