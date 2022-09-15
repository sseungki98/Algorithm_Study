import sys
input=sys.stdin.readline

def find_bomb():
    bomb=[]
    for i in range(R):
        for j in range(C):
            if graph[i][j]=='O':
                bomb.append([i,j])
    return bomb

def set_bomb():
    for i in range(R):
        for j in range(C):
            if graph[i][j]=='.':
                graph[i][j]='O'

def bombing():
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while bomb:
        x,y=bomb.pop()
        graph[x][y]='.'
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                graph[nx][ny]='.'
    
dx=[-1,0,1,0]
dy=[0,1,0,-1]

R,C,N=map(int,input().split())
graph=[list(map(str,input().strip())) for _ in range(R)]

N-=1                    #처음 1초동안은 아무일도 일어나지 않는다.

while N:
    bomb=find_bomb()    #폭탄의 위치 찾기
    set_bomb()          #폭탄 설치
    N-=1
    if N==0:
        break
    bombing()           #폭탄 터뜨리기
    N-=1

for i in range(R):
    print("".join(map(str,graph[i])))
    
#폭탄은 특정 시간을 규칙으로 반복됨으로, 이를 응용하면 시간단축 가능
