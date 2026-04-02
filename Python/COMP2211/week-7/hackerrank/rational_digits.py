if __name__ == '__main__':
    n, d, k = map(int, input().split())

    # remainder at digit k
    r = (n * pow(10, k, d)) % d

    ans = []

    for _ in range(4):
        r *= 10
        ans.append(str(r // d))
        r %= d

    print("".join(ans))
