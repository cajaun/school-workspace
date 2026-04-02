def cubic_series(n):
  
  if n == 1:
    return 1
  else:
    return n**3 + cubic_series(n -1)
  
print(cubic_series(5))