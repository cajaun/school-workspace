def skip_power(n, k):
  
  
  if n < 0:
    return 0
  
  if n < k:
    return n
  else:
    return n**k + skip_power(n-k, k)
  
# print(skip_power(10,3))
# print(skip_power(10,4))
# print(skip_power(3,6))
# print(skip_power(-1,6))