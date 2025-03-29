def ifactorial(n):
  
  def helper(x, result):
    if x == 1:
      return result
    else:
      return helper(x -1, result * x)
    
  if n<= 1:
    return  1
    
  return helper(n,1)

print(ifactorial(5))