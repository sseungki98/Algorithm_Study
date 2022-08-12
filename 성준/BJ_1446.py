N,D=map(int,input().split())
distance=[i for i in range(D+1)]
graph=[]

for _ in range(N):
    s,f,l=map(int,input().split())
    if f > D or f-s<=l:
        continue
    graph.append([s,f,l])
    
for i in range(D+1):  #전 길에서 한칸 건너온 경우와, 지름길로 온 경로를 비교
    distance[i]=min(distance[i],distance[i-1]+1)
    
    for x,y,sc in graph:  #지름길로 해당 위치까지 더 빠르게 갈 수 있다면 해당 위치까지의 거리값을 변경
        if x==i and distance[x]+sc < distance[y]:
            distance[y]=min(distance[x]+sc,distance[y])
            
print(distance[D])
