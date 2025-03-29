def make_empty_tree():
  return ("btree", [])


def makeTree(root, left,right):
  
  return ("btree", [root, left, right])

def root(tree):
  
  return tree[1][0]



def leftSubTree(tree):
  
  return tree[1][1]

def rightSubTree(tree):
  
  return tree[1][2]


def isEmptyTree(tree):
  
  return len(tree[1]) == 0


def isbTree(tree):
  
  return tree[0] == "btree" and isinstance(tree[1], list) and isinstance(tree, tuple)


def isLeafTree(tree):
  
  return len(leftSubTree(tree)) == 0 and len(rightSubTree(tree)) == 0

def countNodes(tree):
  
  if isEmptyTree(tree):
    return 0
  else:
    return 1 + countNodes(leftSubTree(tree)) + countNodes(rightSubTree(tree))


def sumTree(tree):
  
  if isEmptyTree(tree):
    return 0
  else:
    return sumTree(leftSubTree(tree)) + sumTree(rightSubTree(tree)) + root(tree) 
  
def flatten(tree):
  
  if isEmptyTree(tree):
    return []
  else:
    return flatten(leftSubTree(tree)) + [root(tree)] + flatten(rightSubTree(tree))
  
t1 = makeTree (7, makeTree (5, make_empty_tree(), make_empty_tree()) ,makeTree(11, makeTree( 9,
make_empty_tree(),make_empty_tree()), make_empty_tree()))


def interleave(lst1, lst2):
    if lst1 == []:
        return lst2
    elif lst2 == []:
        return lst1
    else:
        return [lst1[0], lst2[0]] + interleave(lst1[1:], lst2[1:])

def split(lst):
  length = len(lst)
  
  return (lst[:length//2], lst[length//2:])


def shuffle(step, lst):
  
  if step == 0:
    return lst
  else:
    return shuffle(step - 1, interleave(split(lst)))
  
def volume(bead):
  
  return 3.14 * bead["diameter"]**3 / 6


def density(bead):
  
  return bead["weight"]/ volume(bead)


def listDensities(beadList):
  return list(map(density, beadList))

def listDensitites2(beadList):
  
  return [density(bead) for bead in range(beadList)]


def findFloaters(beadList):
  
  return list(filter(lambda bead: density(bead) < 1.0, beadList))


def foldr(combiner, base, lst):
  
  if lst == []:
    return base
  else:
    return combiner(lst[0], foldr(combiner, base, lst[1]))
  
  
def heaviestFloater(beadList):
  
  def heavier(bead1, bead2):
    if bead1['weight'] > bead2["weight"]:
      return bead1
    else: 
      return bead2
    
  floaters = findFloaters(beadList)
  
  if floaters == []:
    return None
  else:
    return foldr(heavier, beadList[0], floaters)
    

print(interleave([1, 2, 3], [4, 5, 6, 7]))
print(flatten(t1))
print(sumTree(t1))

