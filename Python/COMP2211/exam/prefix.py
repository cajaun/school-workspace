def mkPrefixSum(arr):
    n = len(arr)
    P = [0] * (n + 1)
    
    for i in range(1, n + 1):
        P[i] = P[i - 1] + arr[i - 1]
    
    return P
  
def getResponses(arr, queries):
    P = mkPrefixSum(arr)
    results = []
    
    for a, b in queries:
        results.append(P[b + 1] - P[a])
    
    return results