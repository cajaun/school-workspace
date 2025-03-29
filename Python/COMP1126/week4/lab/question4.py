from question2 import isPrime

def primeTime(x, y):
  
  if (x > y):
    return "The first value should be less than the second value"
  
  
  for num in range(x, y + 1):
    
    if isPrime(num):
      difference = num - x
      if isPrime(difference):

        print(f"{num}", end = ",")
        

    
    
    
print(primeTime(2, 200))
print(primeTime(2, 300))