def isPrime(n):
  
  if (n < 2):
    return False
  
  for i in range(2, n ):
    
    if (n % i == 0):
      return False

  return True


print(isPrime(13))
print(isPrime(15))
    