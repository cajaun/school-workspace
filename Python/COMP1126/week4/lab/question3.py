from question2 import isPrime

    
def trickWithPrime(x, y):
  
  if (x <= 3):
    return "First number cannot be equal or less than 3"
  
  for num in range(x, y + 1):
    
    if (isPrime(num)):
      square = num * num
      add = square + 29
      remainder = add % 8
      print(f"The prime number is: {num} ")
      print("\U0001F601"  * remainder)
  
      
      
print(trickWithPrime(4, 20))
print(trickWithPrime(2, 20))
  
  