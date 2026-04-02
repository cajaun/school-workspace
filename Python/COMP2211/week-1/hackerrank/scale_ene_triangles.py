if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = int(n), int(k)

    # Arithmetic series formula:
    # total = n/2 * (2 + (n - 1) * k)
    total = n * (2 + (n - 1) * k) // 2

    print(total)