# ID Number: 620169526

# Hackerrank Handle: valmiera

# Hackerrank Exercise: Simple Functions: Auto-Scheduler

# Code submission from Hackerrank: 

def busySchedule(sh, sm, eh, em, m):
  
  startHour = sh * 60
  startTime = startHour + sm

  endHour = eh * 60
  endTime = endHour + em

  if endTime < startTime:
    endTime += 24 * 60  


  length = endTime - startTime

  if (length >= m ):
    return length - m
  else:
    return -1
  
  
    
  
  
  