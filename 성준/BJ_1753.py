import sys
import heapq
from collections import deque
input=sys.stdin.readline

V,E=map(int,input().split())
K=int(input())
graph={i+1:{} for i in range(V)}
visited=[float('inf')]*V
visited[K-1]=0                      #K까지의 거리는 0으로 설정

def bfs():
    dq=[]
    heapq.heappush(dq,(0,K))        #초기값은 K에서 시작하며 누적 가중치는 0
    
    while dq:
        w,node=heapq.heappop(dq)    #가장 짧은 거리부터 탐색하므로, 불필요한 간선의 탐색 시간을 줄일 수 있게 된다.
        
        if visited[node-1]<w:       #현재 노드로 오는 오는 거리보다 w의 무게가 크다면 무시한다.
            continue
        
        for v in graph[node]:       #현재 노드에 연결된 간선 탐색
            n_w=w+graph[node][v]    #누적 가중치를 계산
            if n_w < visited[v-1]:  #더 빠르게 다음 노드로 이동 가능하다면 갱신
                visited[v-1]=n_w
                heapq.heappush(dq,(n_w,v))  #우선순위 큐에 삽입
            
for i in range(E):
    u,v,w=map(int,input().split())
    if v not in graph[u]: graph[u][v]=w
    else: graph[u][v]=min(graph[u][v],w)

bfs()
for v in visited: print(str(v).upper())   #inf로 저장된 값을 INF로 출력하기 위해 str로 변형하여 출력
