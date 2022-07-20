from sys import stdin

N,M=map(int,stdin.readline().split())
structure=[list(map(str,stdin.readline().strip())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
answer=0

def bfs(x,y,ty):  #자신의 옆을 탐색
    visited[x][y]=1
    if ty:  #'-'모양일 경우
        dy=y+1
        if dy<M and structure[x][dy]=='-':
            bfs(x,dy,1)
    else: #'|'모양일 경우
        dx=x+1
        if dx<N and structure[dx][y]=='|':
            bfs(dx,y,0)

for i in range(N):
    for j in range(M):
        if not visited[i][j]: #방문하지 않은 경우
            if structure[i][j]=='-':  #'-'모양일 경우 자신의 오른쪽에 '-'모양이면 해당 위치로 이동
                dy=j+1
                if dy<M and structure[i][dy]=='-':
                    bfs(i,dy,1)
            else: #'|'모양일 경우 자신의 아래쪽에 '|'모양이면 해당 위치로 이동
                dx=i+1
                if dx<N and structure[dx][j]=='|':
                    bfs(dx,j,0)
            answer+=1
print(answer)
