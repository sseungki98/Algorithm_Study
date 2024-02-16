from collections import defaultdict
from collections import deque
N, M, V = map(int, input().split())
route = defaultdict(list)
bfs_route = []
dfs_route = []

for _ in range(M):
    start, end = map(int, input().split())
    route[start].append(end)
    route[end].append(start)


def bfs(node):
    dq = deque()
    visited = []
    dq.append(node)
    visited.append(node)
    while dq:
        target = dq.popleft()
        bfs_route.append(target)
        for item in sorted(route[target]):
            if item not in visited:
                dq.append(item)
                visited.append(item)


def dfs(node, visited):
    visited.append(node)
    dfs_route.append(node)
    for item in sorted(route[node]):
        if item not in visited:
            dfs(item, visited)


visited = []
dfs(V, visited)
bfs(V)
print(*dfs_route)
print(*bfs_route)





