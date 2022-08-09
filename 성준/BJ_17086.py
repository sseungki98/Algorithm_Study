from sys import stdin
input=stdin.readline

N,M=map(int,input().split())
sea=[list(map(int,input().split())) for _ in range(N)]
shark=[]
distance=[[0]*M for _ in range(N)]

for i in range(N):  #상어의 위치 찾기
    for j in range(M):
        if sea[i][j]:
            shark.append([i,j])

for i in range(N):
    for j in range(M):
        if not sea[i][j]:
            tmp=[]
            for x,y in shark:
                tmp.append(max(abs(x-i),abs(y-j)))  #상어와의 거리 계산
            distance[i][j]=min(tmp) #인접한 상어와의 거리 찾기 
            
print(max(map(max,distance))) 
