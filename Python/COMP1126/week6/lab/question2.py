def encodedString(string):
  
  
  newOrd = ""
  for character in string:
    
    if ord(character) % 2 == 0:
      newOrd += chr(ord(character) + 4)
    else:
      newOrd += chr(ord(character) + 2)
      
  
  return newOrd


# print(encodedString("hello"))
      