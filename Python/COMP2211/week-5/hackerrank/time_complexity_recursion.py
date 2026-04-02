from functools import lru_cache

def countOperations(queries):


    def bar_cost(k: int) -> int:

        if k < 2:
            return 0
        S = (k - 2) * (k - 1) // 2
        return 5 * S + 2 * (k - 2)

    @lru_cache(None)
    def T(n: int) -> int:
        if n == 0:
            return 1  

        if n % 3 == 0:
          
            return 4 + T(n // 3) + n * (2 + bar_cost(n * n))

        elif n % 3 == 1:

            return 7 + T(n - 1) + bar_cost(n)

        else:

            return 7 + T(n - 2) + 2 * (n - 2)

    return [T(n) for n in queries]