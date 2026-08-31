def compose(f, g, m):
    (af, bf) = f
    (ag, bg) = g

    a = (af * ag) % m
    b = (af * bg + bf) % m

    return (a, b)
  
def repeated(n, m, g):
    (a, b) = g

    if n == 0:
        return (1, 0)

    elif n % 2 == 0:
        half = repeated(n // 2, m, g)
        return compose(half, half, m)

    else:
        prev = repeated(n - 1, m, g)
        return compose(g, prev, m)
      
def apply(g, m, x):
    (a, b) = g
    return (a * x + b) % m

  
def computeF(n, a, b, m, c):
    return apply(repeated(n, m, (a, b)), m, c)