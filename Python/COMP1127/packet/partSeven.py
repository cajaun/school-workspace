from partSix import pushProjectStack
from partFive import addToPacketQ


def sortPackets(scoreList, stack, queue):
    for pkt, pkt_score in scoreList[1]: 
        if pkt_score > 5.00:  
            stack = pushProjectStack(pkt, stack)
        else: 
            queue = addToPacketQ(pkt, queue)

    return stack, queue