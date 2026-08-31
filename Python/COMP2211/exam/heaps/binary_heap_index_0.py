# heap for index 0

def isEmpty(vec, i):
    return i >= len(vec)

def isLeaf(vec, i):
    return (i < len(vec)) and (2*i + 1 >= len(vec))
  
def left(i):
  return 2 * i + 1

def right(i):
  return 2 * i + 2

def parent(i):
  return (i - 1) // 2

def bubbleUp(vec, i):
  
  while i > 0 and vec [i] < vec[parent(i)]:
    vec[i] = vec[parent(i)]
    vec[parent(i)] = vec[i]
    i = parent(i)
    
