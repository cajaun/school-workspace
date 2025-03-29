def makePacket(pktInfo):
  
  SRC, DST, LEN, PRT, SP, DP, SQN, PLD = pktInfo
  return ("PK", SRC, DST, [LEN, PRT, [SP, DP], SQN, PLD])


def getPacketSrc(pkt):
  
  return pkt[1]


def getPacketDst(pkt):
  
  return pkt[2]


def getPacketDetails(pkt):
  
  return pkt[3]


def isPacket(pkt):
  
  return pkt[0] == "PK" and isinstance(pkt, tuple) and len(pkt[3]) == 4


def isEmptyPkt(pkt):
  
  return len(pkt[3][0]) == 0


# def suspPort(pkt):
  
#   return  getSrcPort(pkt) > 500 or  getDstPort(pkt) > 500


# def suspProto(pkt):
  
#   return  getProtocol(pkt) not in ProtocolList

# def ipBlacklist(pkt):

#     return getPacketSrc(pkt) in IpBlackList


def makeStack():
  
  return ("Stack", [])


def getContents(stk):
  
  if isStack(stk):
    return stk[1]
  raise "Error not a stack"

def top(stk):
  
  if not isStackEmpty(stk):
    return stk[1][0]
  
def push(stk, el):
  
  if isStack(stk):
    stk[1].append(el)
    
def pop(stk):
  
  if not isStackEmpty(stk):
    stk[1].pop(0)

def isStackEmpty(stk):
  
  return len(stk[1]) == 0


def isStack(stk):
  
  return stk[0] == "Stack" and isinstance(stk, tuple) and isinstance(stk[1], list)
  

def squareDouble(l1,l2):
  return [(x**2,y*2) for x in l1 for y in l2]

print(squareDouble([1,2,4], [9,11]))


def countryMin(countries, minimum, maximum):
  
  return list(filter(lambda country: minimum <= countries[country][1] <= maximum, countries))

countries = {
    "Jamaica": [2881000, 1400000, 1481000],
    "Trinidad and Tobago": [1365000, 365000, 1000000],
    "Barbados": [285000, 142500, 142500],
    "USA": [323000000, 123000000, 200000000],
    "Canada": [36290000, 6290000, 3000000],
    "Great Britain": [65640000, 23000000, 42640000],
}

print(countryMin(countries, 1000000, 20000000))



def isDivisor(a,b):
  
  return  b % a == 0


def multipleList(a,b):
  
  return [i for i in range(a, b + 1) if isDivisor(i,b) ]



def oddNumberSumList(lst):
  
  return sum([i for i in range(len(lst)) if i % 2 != 0])


def strangelyOddOrNot(a,b):
  
  res = oddNumberSumList(multipleList(a,b))
  if res % 2 != 0:
    return "Strangely Odd"
  else:
    return "Not really Strangely odd"


  