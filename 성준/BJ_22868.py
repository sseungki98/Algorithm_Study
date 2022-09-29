import sys
from collections import deque

N,M=map(int,input().split())
graph={i+1:[] for i in range(N)}
answer=10000

for i in range(M):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,N+1):              #S->E 까지 사전순으로 우선순위를 가져야 하므로, 각 연결점을 오름차순으로 정렬해준다.
    graph[i].sort() 
    
start,end=map(int,input().split())    
dq=deque([(start,[])])
visited=[0]*(N+1)
answer=[]

visited[start]=1                    #처음 반환점까지는 출발점에 다다르지 않기 위해 방문체크를 해준다.

while True:                         #S->E 까지의 최단거리이므로 bfs를 통해 탐색한다. (#이때, 우선순위큐와 함께 쓰는 bfs는 특정 조건을 만족할 때만 사용하므로 사용X)
    x,path=dq.popleft()
    
    if x==end:
        answer=path
        break
    
    for i in graph[x]:
        if not visited[i]:
            dq.append((i,path+[i]))
            visited[i]=1

visited=[0]*(N+1)
for i in answer:                    #처음 반환점 까지 방문한 모든 노드를 방문확인하여준다.
    visited[i]=1
dq=deque([(end,answer)])

while True:                         #E->S 까지의 최소거리를 탐색한다.
    x,path=dq.popleft()

    if x==start:          
        print(len(path))
        break
    
    for i in graph[x]:
        if not visited[i]:
            dq.append((i,path+[i]))
            visited[i]=1
