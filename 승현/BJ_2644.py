from collections import deque

n = int(input())
a, b = map(int, input().split())
r_n = int(input())


def bfs(node):
    dq = deque()
    dq.append(node)
    while dq:
        node = dq.popleft()
        for item in graph[node]:
            if counts[item] == 0:
                counts[item] = counts[node] + 1
                dq.append(item)


graph = [[] for _ in range(n+1)] # [0부터 10까지], n = 9
for _ in range(r_n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

counts = [0] * (n+1)

bfs(a)
print(counts[b] if counts[b] > 0 else -1)




