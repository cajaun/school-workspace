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