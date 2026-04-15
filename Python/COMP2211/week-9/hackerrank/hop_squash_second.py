from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

idx = 0

# Step 1: vegetable types
k = int(data[idx])
idx += 1

name_to_index = {}
butternut_index = -1

for i in range(k):
    name = data[idx]
    name_to_index[name] = i
    if name == "Butternut Squash":
        butternut_index = i
    idx += 1

# Step 2: patches
n = int(data[idx])
idx += 1

patch_type = [0] * (n + 1)
patch_qty = [0] * (n + 1)

for i in range(1, n + 1):
    v, q = map(int, data[idx].split())
    patch_type[i] = v
    patch_qty[i] = q
    idx += 1

# Step 3: graph
m = int(data[idx])
idx += 1

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    s, t = map(int, data[idx].split())
    adj[s].append(t)
    adj[t].append(s)
    idx += 1

# Step 4: BFS from node 0
visited = [False] * (n + 1)
queue = deque([0])
visited[0] = True

result = 0

while queue:
    node = queue.popleft()

    for neighbor in adj[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)

            if patch_type[neighbor] == butternut_index:
                result += patch_qty[neighbor]

print(result)