import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def check(x,y):
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and ground[nx][ny]:
            check(nx,ny)

T=int(input())
for _ in range(T):
    M,N,K=map(int,input().split())
    ground=[[0]*M for _ in range(N)]
    visited=[[0]*M for _ in range(N)]
    answer=0
    
    for _ in range(K):
        y,x=map(int,input().split())
        ground[x][y]=1

    for i in range(N):
        for j in range(M):
            if ground[i][j] and not visited[i][j]:
                check(i,j)
                answer+=1
    print(answer)
