"""
Group information:


Member 1: 620169526 (valmiera)
Member 2: 

"""


import math
import os
import random
import re
import sys

# Part 1 

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
  
  
  
# Part 2


def getLength(pkt):

    return pkt[3][0]

def getProtocol(pkt):

    return pkt[3][1]

def getSrcPort(pkt):

    return pkt[3][2][0]

def getDstPort(pkt):

    return pkt[3][2][1]

def getSqn(pkt):

    return pkt[3][3]

def getPayloadSize(pkt):

    return pkt[3][4]
  
  
# Part 3

def flowAverage(pktList):

    averagePayLoadSize = sum(getPayloadSize(packet) for packet in pktList) / len (pktList)
    
    return [packet for packet in pktList if getPayloadSize(packet) > averagePayLoadSize]

def suspPort(pkt):

    return getSrcPort(pkt) > 500 or getDstPort(pkt) > 500

def suspProto(pkt):

    return getProtocol(pkt) not in ProtocolList

def ipBlacklist(pkt):

    return getPacketSrc(pkt) in IpBlackList
  
  
# Part 4

def calScore(pkt):
    score = 0.0
    
    metrics = {
        "Payload Size": {
            "condition": lambda p: p in flowAverage(pkt_list),
            "points": 3.56,
            "message": lambda p: f"Payload size greater than average. +3.56 points",
            "fail_message": lambda p: f"Payload size NOT greater than average. 0 points"
        },
        "Suspicious Protocol": {
            "condition": suspProto,
            "points": 2.74,
            "message": lambda p: f"Protocol {getProtocol(p)} is suspicious. +2.74 points",
            "fail_message": lambda p: f"Protocol {getProtocol(p)} is NOT suspicious. 0 points"
        },
        "Suspicious Port": {
            "condition": suspPort,
            "points": 1.45,
            "message": lambda p: f"Port {getSrcPort(p)}/{getDstPort(p)} > 1024. +1.45 points",
            "fail_message": lambda p: f"Port {getSrcPort(p)}/{getDstPort(p)} <= 1024. 0 points"
        },
        "IP Blacklist": {
            "condition": ipBlacklist,
            "points": 10.0,
            "message": lambda p: f"Source IP {getPacketSrc(p)} is in blacklist. +10 points",
            "fail_message": lambda p: f"Source IP {getPacketSrc(p)} is NOT in blacklist. 0 points"
        }
    }

    for metric in metrics.values():
        if metric["condition"](pkt):
            score += metric["points"]
            print(f"Packet {pkt}: {metric['message'](pkt)}")
        else:
            print(f"Packet {pkt}: {metric['fail_message'](pkt)}")
    
    print(f"Total score for Packet {pkt}: {round(score, 2)} points")
    
    return round(score, 2) if score > 0 else 0.0


def makeScore(pktLst):
    
    flowAverage(pktLst)
    return ["SCORE", [(packet, calScore(packet)) for packet in pktLst]]

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
  
  
# Part 5


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
    position = get_pos(pkt, queue)
    queue.insert(position, pkt)
    return ("PQ", queue)

def get_pos(pkt, lst):
    packetSqn = getSqn(pkt) 
    for i, queuedPacket in enumerate(lst):
        if packetSqn < getSqn(queuedPacket):
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
  
  
# Part 6

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


# Part 7

def sortPackets(scoreList, stack, queue):
    for packet, packetScore in scoreList[1]: 
        if packetScore > 5.00:  
            stack = pushProjectStack(packet, stack)
        else: 
            queue = addToPacketQ(packet, queue)

    return stack, queue
  
  
# Part 8

def analysePackets(packet_lst):
    global pkt_list

    pkt_list = [makePacket(*pk) for pk in packet_lst] 


    scorelist = makeScore(pkt_list)


    queue = makePacketQueue()
    stack = makePacketStack()


    scored_packets = [] 
    
    for packet in pkt_list:
        pkt_score = calScore(packet)  
        scored_packets.append((packet, pkt_score)) 


    sortPackets(scorelist, stack, queue)


    return queue


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    
    srcIP = str(first_multiple_input[0])
    dstIP = str(first_multiple_input[1])
    length = int(first_multiple_input[2])
    prt = str(first_multiple_input[3])
    sp = int(first_multiple_input[4])
    dp = int(first_multiple_input[5])
    sqn = int(first_multiple_input[6])
    pld = int(first_multiple_input[7])
    
    ProtocolList = ["HTTPS","SMTP","UDP","TCP","DHCP","IRC"]
    IpBlackList = ["213.217.236.184","149.88.83.47","223.70.250.146","169.51.6.136","229.223.169.245"]
    
    packet_List = [
        (srcIP, dstIP, length, prt, sp, dp, sqn, pld),
        ("111.202.230.44", "62.82.29.190", 31, "HTTP", 80, 20, 1562436, 338),
        ("222.57.155.164", "50.168.160.19", 22, "UDP", 790, 5431, 1662435, 812),
        ("333.230.18.207", "213.217.236.184", 56, "IMCP", 501, 5643, 1762434, 3138),
        ("444.221.232.94", "50.168.160.19", 1003, "TCP", 4657, 4875, 1962433, 428),
        ("555.221.232.94", "50.168.160.19", 236, "HTTP", 7753, 5724, 2062432, 48)
    ]

    
    fptr.write('Forward Packets => ' + str(analysePackets(packet_List)) + '\n')
    
    fptr.close()