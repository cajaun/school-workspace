from partOne import makePacket, getPacketSrc
from partTwo import getSrcPort, getDstPort, getProtocol,  getPayloadSize

pk1 = makePacket("111.202.230.44","62.82.29.190",31,"HTTP",80,20,1562431,38)
pk2 = makePacket("222.57.155.164","50.168.160.19",22,"UDP",90,5431,1662431,82)
pk3 = makePacket("333.230.18.207","213.217.236.184",56,"IRC",501,5643,1762431,318)
pk4 = makePacket("444.221.232.94","50.168.160.19",1003,"TCP",4657,4875,1962431,428)
pk5 = makePacket("555.221.232.94","50.168.160.19",236,"TCP",7753,5724,2062431,48)
    
pkt_list = [pk1,pk2,pk3,pk4]
    
ProtocolList = ["HTTP","SMTP","UDP","TCP","DHCP"]
IpBlackList = ["213.217.236.184","444.221.232.94","149.88.83.47","223.70.250.146","169.51.6.136","229.223.169.245"]

def flowAverage(pktList):

    averagePayLoadSize = sum(getPayloadSize(pkt) for pkt in pktList) / len (pktList)
    
    return [pkt for pkt in pktList if getPayloadSize(pkt) > averagePayLoadSize]

def suspPort(pkt):

    return getSrcPort(pkt) > 500 or getDstPort(pkt) > 500

def suspProto(pkt):

    return getProtocol(pkt) not in ProtocolList

def ipBlacklist(pkt):

    return getPacketSrc(pkt) in IpBlackList