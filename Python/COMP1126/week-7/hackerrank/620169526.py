# ID Number: 620169526

# Hackerrank Handle: valmiera

# Hackerrank Exercise: Easy Commute

# Code submission from Hackerrank: 


Map = [("A","B",4),("A","C",2),("B","C",5),
         ("B","D",10),("C","E",3),("E","D",4),("D","F",11)]

def getTime(A,B):
    for path in Map:
        if path[0] == A and path[1] == B:
            return path[2]
        elif path[0] == B and path[1] == A:
            return path[2]
    return -999
  
  
def travelTime(path):
    if len(path) < 2:
        return 0
    

    time = getTime(path[0], path[1])
    
 
    if time == -999:
        return -999  
    

    next_time = travelTime(path[1:])  
    

    if next_time == -999:
        return -999
    else:
        return time + next_time   
      
print(travelTime(["A", "C", "E", "D"]))  
print(travelTime(["A", "C", "D", "F"]))
print(travelTime(["A", "B", "D", "C"]))
print(travelTime(["B", "C", "E", "B"]))