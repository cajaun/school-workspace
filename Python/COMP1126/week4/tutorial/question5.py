def sum(x):
  
   if (x < 2):
     return 0
   
   if (x % 2 == 0 ):
     return x + sum(x - 2)
   else:
     return sum(x - 1)
   
print(sum(9))