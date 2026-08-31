def insertOne(v, i, el):
    if i == 0:
        v[0] = el
    
    elif el >= v[i - 1]:
        v[i] = el
    
    else:
        v[i] = v[i - 1]
        insertOne(v, i - 1, el)
        
def insertionSort(v):
    n = len(v)
    
    for i in range(1, n):
        el = v[i]
        insertOne(v, i, el)
    
    return v
  
print(insertionSort([12, 8, 31, 4, 15, 3, 19]))

# pass 1 
# [8,12,31,4,15,3,19]

# pass 2
# i = 3 el = 4
#  [8,12,31,31,15,3,19]
# i = 2 el = 4
#  [8,12,12,31,15,3,19]
# i = 1 el = 4
#  [8,8,12,31,15,3,19]
# i = 0 el = 4
#  [4,8,12,31,15,3,19]


