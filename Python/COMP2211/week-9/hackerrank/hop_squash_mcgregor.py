#!/bin/python3

import os
from collections import deque, defaultdict

# Complete the findSquashes function below.
def findSquashes(plotDims, thorns, squashes, passages, jump, start):
    n = len(plotDims)
    a, b = jump
    sp, sx, sy = start
    sp -= 1  # make plot index 0-based

    # All legal jump offsets
    moves = set()
    for dx in (a, -a):
        for dy in (b, -b):
            moves.add((dx, dy))
            moves.add((dy, dx))
    moves.discard((0, 0))
    moves = list(moves)

    # Organize thorns and squash by plot
    thorns_by_plot = [set() for _ in range(n)]
    for i, x, y in thorns:
        thorns_by_plot[i - 1].add((x, y))

    squash_by_plot = [dict() for _ in range(n)]
    for i, x, y, q in squashes:
        squash_by_plot[i - 1][(x, y)] = squash_by_plot[i - 1].get((x, y), 0) + q

    # Mark all hole cells
    holes_by_plot = [set() for _ in range(n)]
    for i, xi, yi, j, xj, yj in passages:
        holes_by_plot[i - 1].add((xi, yi))
        holes_by_plot[j - 1].add((xj, yj))

    # Step 1: find connected movement-components inside each plot
    component_weight = []
    hole_to_component = {}
    start_component = None
    next_component_id = 0

    for plot_idx in range(n):
        r, c = plotDims[plot_idx]
        thorn_set = thorns_by_plot[plot_idx]
        squash_map = squash_by_plot[plot_idx]
        hole_set = holes_by_plot[plot_idx]

        comp = [[-1] * c for _ in range(r)]

        for x in range(r):
            for y in range(c):
                if (x, y) in thorn_set or comp[x][y] != -1:
                    continue

                cid = next_component_id
                next_component_id += 1

                total = 0
                q = deque([(x, y)])
                comp[x][y] = cid

                while q:
                    cx, cy = q.popleft()
                    total += squash_map.get((cx, cy), 0)

                    if (cx, cy) in hole_set:
                        hole_to_component[(plot_idx, cx, cy)] = cid

                    if plot_idx == sp and cx == sx and cy == sy:
                        start_component = cid

                    for dx, dy in moves:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < r and 0 <= ny < c:
                            if (nx, ny) not in thorn_set and comp[nx][ny] == -1:
                                comp[nx][ny] = cid
                                q.append((nx, ny))

                component_weight.append(total)

    if start_component is None:
        return 0

    # Step 2: build UNDIRECTED graph between components using passages
    graph = defaultdict(list)

    for i, xi, yi, j, xj, yj in passages:
        u = hole_to_component[(i - 1, xi, yi)]
        v = hole_to_component[(j - 1, xj, yj)]

        if u != v:
            graph[u].append(v)
            graph[v].append(u)

    # Step 3: BFS/DFS over reachable components and sum squash once
    seen = set([start_component])
    q = deque([start_component])
    ans = 0

    while q:
        u = q.popleft()
        ans += component_weight[u]

        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    # Read in plot dimensions: n lines of (r, c)
    plotDims = []
    for _ in range(n):
        plotDims.append(list(map(int, input().rstrip().split())))

    t = int(input())

    # Read thorn locations: t lines of (i, x, y)
    thorns = []
    for _ in range(t):
        thorns.append(list(map(int, input().rstrip().split())))

    s = int(input())

    # Read squash locations: s lines of (i, x, y, q)
    squashes = []
    for _ in range(s):
        squashes.append(list(map(int, input().rstrip().split())))

    m = int(input())

    # Read passages: m lines of ((i, x_i, y_i), (j, x_j, y_j))
    passages = []
    for _ in range(m):
        passages.append(list(map(int, input().rstrip().split())))

    # Read jump parameters a, b
    jump = list(map(int, input().rstrip().split()))

    # Read starting point (pp, px, py)
    start = list(map(int, input().rstrip().split()))

    result = findSquashes(plotDims, thorns, squashes, passages, jump, start)

    fptr.write(str(result) + '\n')
    fptr.close()