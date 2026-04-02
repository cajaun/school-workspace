from collections import deque

def canReach(m, n, a, b, pr, pc, positions):
    visited = [[False] * n for _ in range(m)]

    moves = {
        ( a,  b), ( a, -b), (-a,  b), (-a, -b),
        ( b,  a), ( b, -a), (-b,  a), (-b, -a)
    }

    q = deque()
    q.append((pr, pc))
    visited[pr][pc] = True

    while q:
        r, c = q.popleft()

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))

    result = []
    for r, c in positions:
        result.append(visited[r][c])

    return result