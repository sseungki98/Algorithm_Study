import sys
input=sys.stdin.readline

N,K=map(int,input().split())
rock=list(map(int,input().split()))
visited=[0]*N
visited[0]=1

#앞에서 건널 수 있는 뒤의 돌 찾기
for i in range(N):
    if visited[i]:
        for j in range(i+1,i+K+1):
            if j<N and visited[j]:
                continue
            if j<N and (j-i)*(1+abs(rock[i]-rock[j]))<=K:
                visited[j]=1
             
#현재 위치로 올 수 있는 이 전의 돌 찾기
for i in range(1,N):
    for j in range(i-1,-1,-1):
        if visited[j]==1 and (i-j)*(1+abs(rock[i]-rock[j]))<=K:
            visited[i]=1
            break
        if i-j>K:
            break
            
print(['NO','YES'][visited[-1]]) 
