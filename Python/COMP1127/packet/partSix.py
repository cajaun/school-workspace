def makePacketStack():
    return ("PS", [])


def contentsStack(stk):
    return stk[1] 


def topProjectStack(stk):
    if isEmptyPKStack(stk):
        return None  
    return stk[1][-1] 


def pushProjectStack(pkt, stk):
    stack = stk[1]
    stack.append(pkt)  
    return ("PS", stack)


def popPickupStack(stk):
    if isEmptyPKStack(stk):
        return stk 
    stack = stk[1]
    stack.pop()  
    return ("PS", stack)


def isPKstack(stk):
    return isinstance(stk, tuple) and len(stk) == 2 and stk[0] == "PS" and isinstance(stk[1], list)


def isEmptyPKStack(stk):
    return len(stk[1]) == 0  
