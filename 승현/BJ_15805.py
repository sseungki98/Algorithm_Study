N = int(input())
graph = list(map(int, input().split()))

visited = {}

visited[graph[0]] = -1
for i in range(1, N):
    if graph[i] in visited.keys():
        continue
    else:
        visited[graph[i]] = graph[i-1]

re_visited = sorted(visited.items())
print(len(re_visited))
for i in range(len(re_visited)):
    if i == len(re_visited)-1:
        print(re_visited[i][1], end='')
    else:
        print(re_visited[i][1], end=' ')


