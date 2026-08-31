def merge(lst1, lst2, prec):
    n1, n2 = len(lst1), len(lst2)
    
    result = []
    i = 0
    j = 0
    
    while i < n1 and j < n2:
        if prec(lst1[i], lst2[j]):
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    
    if i == n1:
        result.extend(lst2[j:])
    else:
        result.extend(lst1[i:])
    
    return result
  
def mergeSort(lst, prec):
    n = len(lst)
    
    if n <= 1:
        return lst
    
    else:
        m = n // 2
        
        left = mergeSort(lst[:m], prec)
        right = mergeSort(lst[m:], prec)
        
        return merge(left, right, prec)