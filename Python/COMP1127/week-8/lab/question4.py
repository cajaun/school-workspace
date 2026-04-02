from question2 import complementString
from question3 import longestGap

def binding(s, t):
  
  tComplement = complementString(t)
  tLength = len(t)
  
  bindingSites = [
        i for i in range(len(s) - tLength + 1) 
        if s[i:i + tLength] == tComplement
    ]
  
  if not bindingSites:
      return -1  
  elif len(bindingSites) == 1:
      return bindingSites[0] 
  else:
      return longestGap(tLength, bindingSites)  
    
    
print(binding('TATAGGGATAGGCTAGTATTT', 'TC' ))
  
      
    
  