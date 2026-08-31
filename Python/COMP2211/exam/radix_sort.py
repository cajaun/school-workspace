def radixSort(vec, radix=10):
    k = 8  # number of digits
    current = vec
    
    for phase in range(k):
        
        buckets = [[] for i in range(radix)]
        
        for val in current:
            bidx = getDigit(val, phase, radix)
            buckets[bidx].append(val)
        
        current = []
        
        for b in buckets:
            current.extend(b)
    
    return current
  
def getDigit(val, phase, radix):
    return (val // (radix ** phase)) % radix