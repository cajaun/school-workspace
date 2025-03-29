def makeQueue():
  return ('queue', [])


def contents(q):
  if isQueue(q):
    return q[1]


def isQueue(obj):
  
  return isinstance(obj, tuple) and isinstance(obj[1], list) and obj[0] == "queue"


def enqueue(q,el):
  if isQueue(q):
    q[1].append(el)
    
    
def dequeue(q):
  if  not isQueueEmpty(q):
    q[1].pop(0)
    return q
  
  
def front(q):
  if isQueue(q):
    if not isQueueEmpty(q):
      return q[1][0]
    
def isQueueEmpty(q):
  if isQueue(q):
    return len(q[1] == 0)
    