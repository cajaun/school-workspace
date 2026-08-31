def qsort(v, start, stop):
    if start < stop:

        q = partition(v, start, stop)
        qsort(v, start, q-1)
        qsort(v, q+1 , stop)

def quickSort(v):
    qsort(v, 0 , len(v) -1)
    return 

# naive stable
def partition(v, start, stop):
    pivot = v[start]
    smaller = []
    larger = []
    
    for el in v[start+1: stop+1]:
        if el < pivot:
            smaller.append(el)
        else:
            larger.append(el)
    
    # copy out smaller into v
    i = 0
    while i < len(smaller):
        v[start + i] = smaller[i]
        i += 1
    
    # store the pivot
    q = start + len(smaller)
    v[q] = pivot
    
    # copy out larger into v
    i = 0
    while i < len(larger):
        v[q + 1 + i] = larger[i]
        i += 1
    
    return q

# in place not stable
def partition(v, start, stop):
    pivot = v[start]
    i = start
    j = stop
    
    while i < j:
        # search right for element that belongs on left
        while v[j] > pivot and i < j:
            j -= 1
        if i < j:
            v[i] = v[j]
        
        # search left for element that belongs on right
        while v[i] < pivot and i < j:
            i += 1
        if i < j:
            v[j] = v[i]
    
    # now i == j
    v[i] = pivot
    return i
  
print(quickSort([12, 8, 31, 4, 15, 3, 19]))

# partition

# pass 1
# left [8,4,3]
# right[12,31,15,19]
# copy left [8,4 ,3, 12, 31,15,19]
