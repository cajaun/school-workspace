BASES = [["A", "T"], ["G", "C"]]

def complementChar(character):
  
  for base in BASES:
    
    if base[0] == character:
      return base[1]
    elif base[1] == character:
      return base[0]

  return None


# print(complementChar("A"))
# print(complementChar("T"))
# print(complementChar("C"))
  