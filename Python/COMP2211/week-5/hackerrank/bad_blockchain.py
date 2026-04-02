import math

def f(s, t, v):
    return v * v * v - t * v * v + s * v


def g(s, t, target, v):
    return f(s, t, v) - target


def bisect_root(s, t, target, lo, hi):
    """Find integers bracketing a root of g in [lo, hi]."""
    glo = g(s, t, target, lo)
    ghi = g(s, t, target, hi)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        gmid = g(s, t, target, mid)
        if glo * gmid <= 0:
            hi = mid
            ghi = gmid
        else:
            lo = mid
            glo = gmid
    return lo, hi


def find_root_candidates(s, t, target):
    """Find integers near roots of f(s,t,v) = target."""
    candidates = set()
    
    # Dynamically expand bounds until we bracket all roots
    B = 1
    while g(s, t, target, -B) > 0:
        B *= 2
    while g(s, t, target, B) < 0:
        B *= 2
    
    # Check if f has critical points (where f' = 0)
    # f'(v) = 3v^2 - 2tv + s, discriminant D = t^2 - 3s
    D = t * t - 3 * s
    
    if D <= 0:
        # f is monotone, single root region
        lo, hi = bisect_root(s, t, target, -B, B)
        candidates.add(lo)
        candidates.add(hi)
        return candidates
    
    # f has two critical points dividing into 3 monotone regions
    sqrtD = int(math.sqrt(D))
    c1 = (t - sqrtD) // 3
    c2 = (t + sqrtD) // 3
    
    intervals = [(-B, c1), (c1, c2), (c2, B)]
    
    for lo, hi in intervals:
        if lo >= hi:
            continue
        
        # Check endpoints
        if g(s, t, target, lo) == 0:
            candidates.add(lo)
        if g(s, t, target, hi) == 0:
            candidates.add(hi)
        
        # Check for sign change (root) in this interval
        if g(s, t, target, lo) * g(s, t, target, hi) < 0:
            a, b = bisect_root(s, t, target, lo, hi)
            candidates.add(a)
            candidates.add(b)
    
    return candidates


def validateBlocks(v_0, blocks):
    curr = v_0
    out = []
    
    for s, t in blocks:
        candidates = set()
        
        # Find integers near roots
        roots = find_root_candidates(s, t, curr)
        for r in roots:
            for v in range(r - 4, r + 5):
                candidates.add(v)
        
        # Find the best candidate
        best = None
        best_diff = None
        for v in candidates:
            diff = abs(f(s, t, v) - curr)
            if best is None or diff < best_diff or (diff == best_diff and v < best):
                best = v
                best_diff = diff
        
        out.append(best)
        curr = best
    
    return out
