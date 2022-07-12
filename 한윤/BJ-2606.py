# 2022-07-12 (화)

def dfs(graph, visited, v):
    visited[v] = True # 방문처리

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)

n = int(input()) # n : 컴퓨터의 수
m = int(input()) # m : 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
graph = [[] for _ in range(n + 1)] # 0을 사용하지 않고, 1부터 n까지 사용

for _ in range(m):
    a, b = map(int, input().split()) # 연결되어 있는 컴퓨터 쌍
    # 쌍방향 연결이므로, 양쪽 노드에 연결된 정보를 추가
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1) # 방문처리를 위한 리스트

dfs(graph, visited, 1) # 1번 노드에 대한 dfs 함수 수행

count = -1 # 시작 노드인 1의 count를 하지 않지만, visited엔 True로 표기되므로 -1부터 시작
for i in range(1, len(visited)):
    if visited[i] == True:
        count += 1

print(count) # 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
