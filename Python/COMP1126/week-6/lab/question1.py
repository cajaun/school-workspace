PUNCTUATIONS = [",", ".", "?", "!", ";", ":", "-", "^"]


def excludePunNum(string):
  
  newString = ""
  for characters in string:
    if characters not in PUNCTUATIONS and not characters.isdigit():
      newString += characters
  return newString


# print(excludePunNum("COMP1126!! Sci2023 is a, : lot of, fun?"))

# print(excludePunNum("^_^ LOL We3 l0ove Comp Sci3^33"))
      
  