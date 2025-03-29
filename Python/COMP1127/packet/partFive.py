from partTwo import getSqn

def makePacketQueue():
    return ("PQ", [])
  
def contentsQ(q):
    return q[1]

def frontPacketQ(q):
    if isEmptPacketQ(q):
        return None  
    return q[1][0]

def addToPacketQ(pkt, q):
    queue = q[1]
    pos = get_pos(pkt, queue)
    queue.insert(pos, pkt)
    return ("PQ", queue)

def get_pos(pkt, lst):
    pkt_sqn = getSqn(pkt) 
    for i, queued_pkt in enumerate(lst):
        if pkt_sqn < getSqn(queued_pkt):
            return i
    return len(lst)

def removeFromPacketQ(q):
    if isEmptPacketQ(q):
        return q  
    queue = q[1]
    queue.pop(0)  
    return ("PQ", queue)

def isPacketQ(q):
    return isinstance(q, tuple) and len(q) == 2 and q[0] == "PQ" and isinstance(q[1], list)

def isEmptPacketQ(q):
    return len(q[1]) == 0  