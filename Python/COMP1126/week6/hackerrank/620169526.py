# ID Number: 620169526

# Hackerrank Handle: valmiera

# Hackerrank Exercise: Ciphertext Challenge

# Code submission from Hackerrank: 

def encrypt(message):
  
  cipherText = ""
  for character in message:
    
    if ord(character) % 2 == 0:
      cipherText += chr(ord(character) - 4)
    else:
      cipherText += chr(ord(character) + 4)
    
  return cipherText


print(encrypt("password"))


def decrypt(cipherText):
    decryptedText = ""
    for character in cipherText:

        
        if ord(character) % 2 == 0:  
            decryptedText += chr(ord(character) + 4)
        else:  
            decryptedText += chr(ord(character) - 4)
    
    return decryptedText
  
print(decrypt("python3 ^mkni``sk"))