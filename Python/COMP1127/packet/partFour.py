from  partTwo import  getProtocol, getSrcPort, getDstPort
from partThree import suspProto, suspPort, ipBlacklist, flowAverage
from partOne import getPacketSrc

def calScore(pkt):
    
    
    score = 0.0
    
    # Check for payload size
    if pkt in flowAverage(pkt_list): 
        score += 3.56
        print(f"Packet {pkt}: Payload size greater than average. +3.56 points")
    else:
        print(f"Packet {pkt}: Payload size NOT greater than average. 0 points")
    
    # Check for suspicious protocol
    if suspProto(pkt):
        score += 2.74
        print(f"Packet {pkt}: Protocol {getProtocol(pkt)} is suspicious. +2.74 points")
    else:
        print(f"Packet {pkt}: Protocol {getProtocol(pkt)} is NOT suspicious. 0 points")
    
    # Check for suspicious port
    if suspPort(pkt):
        score += 1.45
        print(f"Packet {pkt}: Port {getSrcPort(pkt)}/{getDstPort(pkt)} > 1024. +1.45 points")
    else:
        print(f"Packet {pkt}: Port {getSrcPort(pkt)}/{getDstPort(pkt)} <= 1024. 0 points")
    
    # Check for IP blacklist
    if ipBlacklist(pkt):
        score += 10.0
        print(f"Packet {pkt}: Source IP {getPacketSrc(pkt)} is in blacklist. +10 points")
    else:
        print(f"Packet {pkt}: Source IP {getPacketSrc(pkt)} is NOT in blacklist. 0 points")
    
    # Final score
    print(f"Total score for Packet {pkt}: {round(score, 2)} points")
    
    return round(score, 2) if score > 0 else 0.0

def makeScore(pktLst):
    
    flowAverage(pktLst)
    return ["SCORE", [(pkt, calScore(pkt)) for pkt in pktLst]]

def addPacket(SLst, pkt):
   
    SLst[1].append((pkt, calScore(pkt)))

def getSuspPkts(Score):
   
    return [pkt for pkt, score in Score[1] if score > 5]

def getRegulPkts(Score):

    return [pkt for pkt, score in Score[1] if score <= 5]

def isScore(Score):

    return isinstance(Score, list) and Score[0] == "SCORE" and isinstance(Score[1], list)

def isEmptyScore(Score):

    return len(Score[1]) == 0