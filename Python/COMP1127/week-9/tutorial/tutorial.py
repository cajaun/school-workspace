def make_empty_tree():
  return ("btree", [root, [], []])


def makeTree(root, left, right):
  
  return ("btree", [root, left, right])


def root(tree):
  
  return tree[1][0]


def leftSubTree(tree):
  
  return tree[1][1]

def rightSubTree(tree):

  return tree[1][2]


def isEmptyTree(tree):
  
  return len(leftSubTree(tree)) == 0 and len(rightSubTree(tree)) == 0


def isbTree(tree):
  
  return isinstance(tree, tuple) and tree[0] == "btree" and isinstance(tree[1], list) and len(tree[1] == 3)


def isLeafTree(tree):
  
  return len(leftSubTree(tree)) == 0 and len(rightSubTree(tree) == 0)


def preorder(tree):
  
  if isEmptyTree(tree):
    return []
  
  else:
    
    return [root(tree) + preorder(leftSubTree(tree)) + preorder(rightSubTree(tree))]
  
  
def inorder(tree):
  
  if isEmptyTree(tree):
    return []
  else:
    return [root(tree) + inorder(leftSubTree(tree)) + inorder(rightSubTree(tree))]
  

def sumTree(tree):
    if isEmptyTree(tree):  
        return 0
    return root(tree) + sumTree(leftSubTree(tree)) + sumTree(rightSubTree(tree)) 
  
def maxTree(tree):
  if isEmptyTree(tree):
    return float('-inf')
  else:
    return max(root(tree), maxTree(leftSubTree(tree)), maxTree(rightSubTree(tree)))
  
  
def countNodes(tree):
  if isEmptyTree(tree):
    return 0
  return 1 + countNodes(leftSubTree(tree)) + countNodes(rightSubTree(tree))
  
t1 = makeTree (7, makeTree (5, make_empty_tree(), make_empty_tree()) ,makeTree(11, makeTree( 9,
make_empty_tree(),make_empty_tree()), make_empty_tree()))

print(sumTree(t1))