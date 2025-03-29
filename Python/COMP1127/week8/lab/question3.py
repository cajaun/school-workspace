def longestGap(ln, lst):
  
  if len(lst) < 2:
      return 0  

  gaps = []

  for i in range(1, len(lst)):
      gap = (lst[i] - lst[i - 1]) - ln
      gaps.append(gap)

  return max(gaps) 

# print(longestGap(2, [3, 9, 20]))
    