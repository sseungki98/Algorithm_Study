import sys
from sys import stdin
sys.setrecursionlimit(10**6)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y,c): #일반사람 기준 너비 우선 탐색
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and color[nx][ny]==c:
            bfs(nx,ny,c)

def bfs_special(x,y,c): #적록색약 기준 너비 우선 탐색
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and color_special[nx][ny]==c:
            bfs_special(nx,ny,c)
            
N=int(stdin.readline())
color=[list(map(str,stdin.readline().strip())) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
answer_normal=0
answer_special=0

color_special=[]
for col in color:   #색약을 위한 영역 변경
    tmp=[]
    for c in col:
        c=c.replace('R','G')  #'R'과 'G'를 동일시하게 보기 때문에 R을 G로 대체
        tmp.append(c)
    color_special.append(tmp)

for i in range(N):  #일반 사람이 구분 가능한 영역 찾기
    for j in range(N):
        if not visited[i][j]:
            visited[i][j]=1
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and color[nx][ny]==color[i][j]:
                    bfs(nx,ny,color[i][j])
            answer_normal+=1
            
visited=[[0]*N for _ in range(N)]

for i in range(N):  #적록 색약이 구분 가능한 영역 찾기
    for j in range(N):
        if not visited[i][j]:
            visited[i][j]=1
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and color_special[nx][ny]==color_special[i][j]:
                    bfs_special(nx,ny,color_special[i][j])
            answer_special+=1
print(answer_normal,answer_special)
