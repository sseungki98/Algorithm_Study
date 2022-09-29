def dfs(idx,top,bottom):
    if not visited[idx]:            #idx번째 노드가 방문되어 있지 않다면
        visited[idx]=1  
        for k in graph[idx]:        #idx번째 노드가 연결된 노드를 탐색
            top.add(idx)            #위의 출발 노드 idx를 추가
            bottom.add(k)           #도착 노드 k를 추가
            
            if top==bottom:         #출발 노드의 집합과, 도착노드의 집합이 같다면
                answer.extend(list(bottom))     #정답에 요소 추가
                return
            
            dfs(k,top,bottom)
            
    visited[idx]=0

N=int(input())
graph={i+1:[] for i in range(N+1)}    #각 노드에 연결된 방향 노드로 생각
answer=[]

for i in range(1,N+1):  
    node=int(input())
    graph[i].append(node)
    
for i in range(1,N+1):          
    visited=[0]*(N+1)
    dfs(i,set(),set())

answer=sorted(list(set(answer)))

print(len(answer))
print(*answer,sep='\n')
