def factModSum(arr):
    MOD = 10**9

    # Precompute factorials up to 44! modulo MOD
    fact = [1] * 45
    for i in range(1, 45):
        fact[i] = (fact[i - 1] * i) % MOD

    total = 0
    for x in arr:
        if x < 45:
            total = (total + fact[x]) % MOD
        # else: contribution is 0

    return total