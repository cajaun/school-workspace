import sys

def solve():
    data = sys.stdin.buffer.read().splitlines()
    n = int(data[0])
    lo = 0
    hi = 0

    for i in range(1, n + 1):
        parts = data[i].split()
        op = parts[0]

        if op == b'ADD':
            v = int(parts[1])
            # either keep x, or do x+v
            hi = max(hi, hi + v)
            lo = min(lo, lo + v)

        elif op == b'LDI':
            v = int(parts[1])
            # either keep x, or set to v
            hi = max(hi, v)
            lo = min(lo, v)

        else:  # SQR
            # either keep x, or square it
            sq_max = lo * lo
            hh = hi * hi
            if hh > sq_max:
                sq_max = hh
            if sq_max > hi:
                hi = sq_max
            # lo unchanged (skipping keeps old lo reachable)

    sys.stdout.write(str(hi))