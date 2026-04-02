def computedSquare(n):
  
  a = 1

  while a * a < n:
    b = 1
    while b * b < n:
      if (a * a + b *  b == n):
        return True
      b += 1
    a += 1
  return False
  

print(computedSquare(225))
print(computedSquare(64))
print(computedSquare(-225))
print(computedSquare(2))
print(computedSquare(65))

