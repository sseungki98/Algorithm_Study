def dfs(x):
    visited[x-1]=1
    for val in node[x]:
        if not visited[val-1]:
            dfs(val)

N=int(input())
K=int(input())
node={}
visited=[0]*N
visited[0]=1

for i in range(N):
    node[i+1]=[]
for k in range(K):  #간선으로 이어진 노드를 연결해준다.
    a,b=map(int,input().split())
    node[a].append(b)
    node[b].append(a)
for val in node[1]: #노드 1과 연결되있는 지점들부터 탐색을 시작한다.
    if not visited[val-1]:
        dfs(val)

print(visited.count(1)-1) #1번 노드를 제외하고 방문한 노드의 갯수를 카운트한다.
