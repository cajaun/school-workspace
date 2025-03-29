from question1 import complementChar
BASES = [["A", "T"], ["G", "C"]]

def complementString(string):
  
  dna = ""

  for character in string:
    complement = complementChar(character)
    
    if complement:
      dna += complement
    else:
      return None
  return  dna

# print(complementString("ATCG"))
  