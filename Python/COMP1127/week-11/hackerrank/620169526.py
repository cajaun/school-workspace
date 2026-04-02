import heapq

arrival_order = 0

# Function to create an aircraft object as a tuple (fuel level, arrival order, ID)
def mkAircraft(iD, fuelLvl):
    global arrival_order
    aircraft = (fuelLvl, arrival_order, iD)  
    arrival_order += 1  
    return aircraft


def getiD(node):
    return node[2]


def getFuelLvl(node):
    return node[0]

def mkPriorityQueue():
    return []


def isPriQueueEmpty(priqContents):
    return len(priqContents) == 0


def addAirCraftToQueue(priQueue, aircraft):
    heapq.heappush(priQueue, aircraft)


def popAirCraftFromQueue(priQueue):
    return heapq.heappop(priQueue) if priQueue else None


if __name__ == '__main__':
    c = int(input().strip())
    priority_queue = mkPriorityQueue()
    
    for _ in range(c):
        command = input().strip().split()
        
        if command[0] == "add":
            aircraft_id = command[1]
            fuel_level = int(command[2])
            aircraft = mkAircraft(aircraft_id, fuel_level)
            addAirCraftToQueue(priority_queue, aircraft)
        
        elif command[0] == "land":
            if not isPriQueueEmpty(priority_queue):
                landed_aircraft = popAirCraftFromQueue(priority_queue)
                print(getiD(landed_aircraft))