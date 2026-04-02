from question1 import excludePunNum
from question2 import encodedString 
from question3 import decodedString


def stringList(string):
 return string.split()

def encodedList(array):
  
  if array == []:
    return []
  else:
    return encodedList(array[1:]) + [encodedString(array[0])] 
  
  
print(encodedList(['This', 'is', 'a', 'test', 'drill']))


def decodedList(array):
  
  if array == []:
    return []
  else:
    return decodedList(array[1:]) + [decodedString(array[0])] 
  
  
print(decodedList(['hvkpp', 'xgux', 'c', 'ku', 'Xlku']))



def main(s):
  slst=excludePunNum(s)
  eList = encodedList(stringList(slst))
  dList = decodedList(eList)
  print("Given string =>", s)
  print("Punctuation removed =>", slst)
  print("List Encoded =>", eList)
  print("List Decoded =>", dList)
  print("Encoded Message =>",' '.join(eList))
  
  
print(main("COMP1126!! Sci2023 is a, : lot of, fun?"))


  
      
  