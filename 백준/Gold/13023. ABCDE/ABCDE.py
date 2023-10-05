from collections import defaultdict
store = defaultdict(set)
arrive = False

def input_and_split():
    a, b = map(int, input().split())
    return a, b


M, N = input_and_split()

def dfs(start, visited):
    global arrive
    visited.append(start)
    if len(visited) == 5:
        arrive = True
        return

    for item in store[start]:
        if item not in visited:
            dfs(item, visited)
            visited.pop()

    return visited


for _ in range(N):
    t1, t2 = input_and_split()
    store[t1].add(t2)
    store[t2].add(t1)


for i in range(M):
    visited = []
    dfs(i, visited)
    if arrive:
        print(1)
        break

if not arrive:
    print(0)
