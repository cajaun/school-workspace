def cons(x, y):
    return [x, y]

def car(p):
    return p[0]

def cdr(p):
    return p[1]

nil = []

def makeBinTree(root, left, right):
    return cons(left, cons(root, right))

emptyTree = nil


def isEmpty(tree):
    return tree == nil


def root(tree):

    return car(cdr(tree))


def left(tree):
    return car(tree)


def right(tree):
    return cdr(cdr(tree))


def isLeaf(tree):
    return (not isEmpty(tree)) and isEmpty(left(tree)) and isEmpty(right(tree))



def findNumSpecialPaths(tree, secret, low, high):

    count = 0

    def dfs(node, running_mod, treasure_count):
        nonlocal count

        if isEmpty(node):
            return


        running_mod = (running_mod + root(node)) % secret


        if running_mod == 0:
            treasure_count += 1


        if isLeaf(node):
            if low <= treasure_count <= high:
                count += 1
            return

        dfs(left(node), running_mod, treasure_count)
        dfs(right(node), running_mod, treasure_count)

    dfs(tree, 0, 0)
    return count



def buildTreeAndSearch(connections, s, l, h):
    n = len(connections)
    nodes = [None] * (n+1)
    nodes[0] = emptyTree
    for (i, v, j, k) in connections:
        nodes[i] = makeBinTree(v, nodes[j], nodes[k])
    r = findNumSpecialPaths(nodes[1], s, l, h)
    return r
