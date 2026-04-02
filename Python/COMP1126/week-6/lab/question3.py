def decodedString(string):

    if not string:
        return ""
    

    firstCharacter = string[0]
    
    ordResult = ord(firstCharacter)
    

    if ordResult % 2 == 0:  
        decodedValue = chr(ordResult - 4)
    else:  
        decodedValue = chr(ordResult - 2)
    

    return decodedValue + decodedString(string[1:])
  

# print(decodedString("lgppq"))
