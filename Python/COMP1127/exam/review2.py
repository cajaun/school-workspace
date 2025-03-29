# def digits(n):
  
#   def countDigits(s):
#     if len(s) == 0:
#       return 0
#     else:
#       return 1 + countDigits(s[1:])
    
#   return countDigits(str(n))


# def lcs(n):
  
#   string = str(n)
#   res = string[1:] + string[0]
  
#   return int(res)



# def oddlist(lst):
#   if lst==[]:
#     return []
#   elif (lst[0]%2==0):
#     return oddlist(lst[1:])
#   else:  
#     return [lst[0]] + oddlist(lst[1:])
  
# print(oddlist([1,2,3,4,5]))





# a={}
# a['a']=1
# a['b']=[2,3,4]
# print(a)







# a={}
# a[1]=1
# a['1']=2
# a[1.0]=4
# count=0
# for i in a:
#  count+=a[i]
# print(count)



# def to_upper(k):
#  return k.upper()
# x=['ab', 'cd']
# print(list(map(to_upper,x)))

# lst1 = [1,2,3,4]
# print(lst1[:-1])

def sum_recursive(x):
  def keeps_adding(a, s):
    if a > x:
      return s
    else:
      return keeps_adding(a + 1, s + a)
  if x == 0:
    return 0
  return keeps_adding(1,0)

# print(sum_recursive(4))

# def is_freezing(w):
#   return w = 0

# def ForFunction3(lst):
#   for el in lst:
#     if(el == 0):
#       lst = lst + [el]
#   return len(lst)

# print(ForFunction3([1,2,3,4,5]))

Map = [("Gym","School",4),
       ("Gym","Office",2),
       ("School","Office",5), 
       ("Home","School",10),
       ("School","Home",3),
       ("Home","Gym",4), 
       ("Office","Home",11),
        ]

# def getTime(X,Y):
#   for path in Map:
#     if path[0 ] == X and path[1] == Y:
#       return path[2]
#     elif path[0] == Y and path[1]== X:
#       return path[2]
#   return -999
  
# print(getTime("Gym", "School"))

# mylst=["COMP1126",[0,1,2,3,4,5,6,7], ["85"], [[1,2,3]]]

# print(mylst[1][-1:-4])





# def stopTime(Time):
#   endOftime = 999

#   if(Time == endOftime-1):
#     return -1

#   time = Time
#   running = Time
#   while time == running:
#     print(time)
#     time +=1
#     running += 1

# print(stopTime(100))        
        
def makeIncidentReportDB():
  
  return []


def makeIncidentReport(address, town, incidentType):
  
  return [address, town, incidentType]


def getTown(r):
  
  return r[1]


def getStreetAddress(r):
  
  return r[0]


def getIncidentType(r):
  
  return r[2]


def addIncidentReport(db, r):
  
  return db.append(r)


def getIncidentPriority(r):
  
  incidentType = getIncidentType(r)
  
  
  incidentTypes = {
    100: "PersonalInjury",
    90: "DownedPowerLine",
    80: "OpenDrain"
  }
  
  return incidentTypes.get(incidentType,"Unknown")



def deleteIncidentReport(db, r):
  
  return db.remove(r)


def isHighPriority(r):
  
  
  return True if getIncidentPriority(r) >= 90 else False



def getHighPriority(db):
  
  return [incident for incident in db if isHighPriority(incident)]



def isDivisor(a,b):
  
  return a % b == 0


def divisorList(a):
  
  return [num for num in range(1 , a) if isDivisor(a, num)]


def sumList(lst):
  
  return sum(lst)


def perfectOrNot(a):
  
  
  res = sumList(divisorList(a))
  
  if res == a:
    return "Perfect"
  elif res > a:
    return "Is Abundant"
  else:
    return "Is Deficient"
  
  
  
print(perfectOrNot(28))
print(perfectOrNot(29))
print(perfectOrNot(30))



def makePotHoleList():
  
  return []


def makePotHole(roadname, distance, size):
  
  return [roadname, distance, size]



def getPotHoleRoad(pothole):
  
  return pothole[0]

def getDistance(pothole):
  
  return pothole[1]

def getSize(pothole):
  
  return pothole[2]


def addPotHole(plist, pothole):
  
  return plist.append(pothole)


def potHolesOnRoad(name, repo):
  
  return list(filter(lambda pothole: getPotHoleRoad(pothole) == name, repo))


def numberOfPotHolesOnRoad(name, repo):
  
  sum = 0
  
  for pothole in repo:
    
    if getPotHoleRoad(pothole) == name:
      sum+= 1
  return sum


def zipWith(f, lst1, lst2):
  
  if lst1 == [] or lst2 == []:
    return []
  else:
    return [f(lst1[0], lst2[0]) + zipWith(f, lst1[1:], lst2[2:])]
  
  
  
def makeQueue():
  
  return ("queue", [])


def contents(q):
  
  return q[1]


def front(q):
  
  return contents(q)[0]


def enqueue(q, el):
  
  if isQueue(q):
    contents(q).append(el)
  else:
    raise TypeError("Not a queue")
  
def dequeue(q):
  
  if not isQueueEmpty(q):
    contents(q).pop(0)
  else:
    
    raise IndexError("Queue is empt")
  
  
def isQueueEmpty(q):
  
  return len(contents(q)) == 0


def isQueue(q):
  
  return isinstance(q, tuple) and q[0] == "queue" and isinstance(q[1], list)



# def countryPopulation(countries, minimum, maximum):
  
#   return [country for country, population in countries.items() if minimum <= population <= maximum ]


countries = {
    "Jamaica": [2881000, 1400000, 1481000],
    "Trinidad and Tobago": [1365000, 365000, 1000000],
    "Barbados": [285000, 142500, 142500],
    "USA": [323000000, 123000000, 200000000],
    "Canada": [36290000, 6290000, 3000000],
    "Great Britain": [65640000, 23000000, 42640000],
}

# print(countryPopulation(countries, 20000, 20000000))


def makeStack():
  return ("stack", [])


def contents(stk):
  
  return stk[1]


def isStk(obj):
  
  return isinstance(obj, tuple) and isinstance(obj[1], list) and obj[0] == "stack"


def push(stk, el):
  
  if isStk(stk):
    contents(stk).append(el)
    
    
 
  