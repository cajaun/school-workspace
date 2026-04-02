def findSecrets(arr, queries):
    MOD = 10**9 + 7
    n = len(arr)

    # prefix products
    prefix = [1] * (n + 1)

    for i in range(1, n + 1):
        prefix[i] = (prefix[i-1] * arr[i-1]) % MOD

    results = []

    for i, j in queries:
        # modular inverse of prefix[i-1]
        inv = pow(prefix[i-1], MOD-2, MOD)

        product = (prefix[j] * inv) % MOD
        results.append(product)

    return results