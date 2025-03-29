from partFive import makePacketQueue 
from partSix import makePacketStack
from partOne import makePacket
from partFour import calScore, makeScore
from partSeven import sortPackets


def analysePackets(packet_lst):
    global pkt_list

    pkt_list = [makePacket(*pk) for pk in packet_lst] 


    scorelist = makeScore(pkt_list)


    queue = makePacketQueue()
    stack = makePacketStack()


    scored_packets = [] 
    
    for pkt in pkt_list:
        pkt_score = calScore(pkt)  
        scored_packets.append((pkt, pkt_score)) 


    sortPackets(scorelist, stack, queue)


    return queue


packet_List = [
    ("111.202.230.44", "62.82.29.190", 3, "HTTP", 80, 3463, 1562431, 87),  
    ("111.202.230.44", "62.82.29.190", 31, "HTTP", 80, 20, 1562436, 38),  
    ("222.57.155.164", "50.168.160.19", 22, "UDP", 90, 5431, 1662435, 82), 
    ("333.230.18.207", "213.217.236.184", 56, "IRC", 501, 5643, 1762434, 318), 
    ("444.221.232.94", "50.168.160.19", 1003, "TCP", 4657, 4875, 1962433, 428),  
    ("555.221.232.94", "50.168.160.19", 236, "TCP", 7753, 5724, 2062432, 48),  
]

print(analysePackets(packet_List))