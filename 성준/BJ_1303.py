dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y,color):
    global tmp_answer   #한번 탐색 할 때 뭉쳐있는 병사의 수 count 
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and soldier[nx][ny]==color:
            dfs(nx,ny,color)
            tmp_answer+=1
            
M,N=map(int,input().split())
soldier=[list(map(str,input().strip())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]

white_team=0
blue_team=0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if soldier[i][j]=='W':        #같은 팀인 white team 병사 찾기
                tmp_answer=1
                dfs(i,j,'W')
                white_team+=tmp_answer**2 #뭉쳐 있는 병사의 수 제곱 
            elif soldier[i][j]=='B':      #같은 팀인 blue team 병사 찾기
                tmp_answer=1
                dfs(i,j,'B')
                blue_team+=tmp_answer**2  #뭉쳐 있는 병사의 수 제곱
                
print(white_team,blue_team)
