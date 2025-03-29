def power2(x):
  
  if x <= 0:
    return 0
  
  def helper(x,y):
    
    if y < 1:
      return  1
    else:
      return x * helper(x, y-1)
    
  return helper(x,x)


print(power2(3))
  
  
