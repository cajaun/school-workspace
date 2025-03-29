def makePacket(srcIP, dstIP, length, prt, sp, dp, sqn, pld):

    return ("PK", srcIP, dstIP, [length, prt, [sp, dp], sqn, pld])
    
def getPacketSrc(pkt):

    return pkt[1]
    
def getPacketDst(pkt):

    return pkt[2]
    
def getPacketDetails(pkt):

    return pkt[3]
    
def isPacket(pkt):

     return isinstance(pkt, tuple) and len(pkt) == 4 and pkt[0] == "PK"

def isEmptyPkt(pkt):

    return not pkt[3]