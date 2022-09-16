import sys
import heapq
input=sys.stdin.readline

a,b=map(int,input().split())
N,M=map(int,input().split())
graph={i+1:[] for i in range(N)}
visited=[10001]*N
visited[a-1]=0
            
for i in range(M):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dq=[]
heapq.heappush(dq,[0,a])

while dq:
    cnt,idx=heapq.heappop(dq)               #거리가 가장 빠른 node부터 pop
    
    if visited[idx-1]<=cnt:
        continue
    
    for i in graph[idx]:
        if visited[i-1]<=visited[idx-1]+1:  #해당 노드로 더 빨리 도착하는 길이 있었다면 이번 반복 무시
            continue
        visited[i-1]=cnt+1
        heapq.heappush(dq,[cnt+1,i])
    
print(visited[b-1] if visited[b-1]!=10001 else -1)  #도달 할 수 없다면 -1 출력
