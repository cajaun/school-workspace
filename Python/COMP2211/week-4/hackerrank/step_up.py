import math
import sys

def feasible(a: int, b: int, c: int, l: int, n: int) -> bool:

    if n <= 0:
        return 0 <= l

    k = n.bit_length() - 1  

    an2 = a * n * n
    term1 = an2 // c
    rem = an2 % c  

    base = term1 + b * n + k  


    if base > l:
        return False
    if base + 1 <= l:
        return True

   
    frac_r = rem / c
    frac_log = math.log2(n) - k  


    return (frac_r + frac_log) < 1.0 - 1e-12


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    a, b, c, l = map(int, data)

    lo, hi = 0, 1
    while feasible(a, b, c, l, hi):
        hi *= 2

    while lo < hi:
        mid = (lo + hi + 1) // 2
        if feasible(a, b, c, l, mid):
            lo = mid
        else:
            hi = mid - 1

    print(lo)