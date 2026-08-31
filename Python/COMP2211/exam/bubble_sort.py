def bubbleSort(lst, prec):
    n = len(lst)
    
    for i in range(n):
        for j in range(n - 1 - i):
            if not prec(lst[j], lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return lst
  
def countSwaps(lst, prec):
    n = len(lst)
    swapCount = 0
    
    for i in range(n):
        for j in range(n - 1 - i):
            if not prec(lst[j], lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapCount += 1
    
    return swapCount