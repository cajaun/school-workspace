def findLargest(s, a, b, m, n, k):
    values = []
    x = s % m  
    for _ in range(n):
        values.append(x)
        x = (x * x + a * x + b) % m
    
    values.sort()
    return values[max(0, n - k):]