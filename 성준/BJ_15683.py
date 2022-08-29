import copy
import sys
input=sys.stdin.readline

mode=[    #각 cctv mode에 따라 회전 가능한 방향 벡터집합
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

dx=[0,-1,0,1]
dy=[1,0,-1,0]

def find_blind_spot(tmp_office):    #사각지대 찾는 함수
    cnt=0
    for i in range(N):
        cnt+=tmp_office[i].count(0)
    return cnt

def convert(t_office,x,y,md):       #cctv를 회전 할 때
    for i in md:                    #설정받은 모드에 따라 각 지역을 탐색
        nx=x
        ny=y
        while 0<=nx<N and 0<=ny<M:  #범위를 벗어나면 종료
            nx+=dx[i]
            ny+=dy[i]
            if 0<=nx<N and 0<=ny<M and t_office[nx][ny]==6:   #벽을 만나면 종료
                break
            if 0<=nx<N and 0<=ny<M and not t_office[nx][ny]:
                t_office[nx][ny]=7
    return t_office
    
def dfs(t_office,idx):
    global cctv,answer
    if idx==len(cctv):                #cctv의 설정이 모두 끝난 후 사각지대 탐색
        answer=min(answer,find_blind_spot(t_office))
        return
    
    x,y,c_type=cctv[idx]
    temp=copy.deepcopy(t_office)
    for i in mode[c_type]:
        temp=convert(temp,x,y,i)      #각 모드에 맞게 cctv 설정
        dfs(temp,idx+1)               #해당 모드로 설정 후 다음 cctv 설정
        temp=copy.deepcopy(t_office)
    
    
N,M=map(int,input().split())
office=[list(map(int,input().split())) for _ in range(N)]
cctv=[]
answer=N*M  #cctv를 설정하지 않았을 때 최댓값은 N*M 으로 설정

for i in range(N):    #cctv 위치를 탐색 후 [x,y,cctv] 종류 입력
    for j in range(M):
        if 1<=office[i][j]<=5:
            cctv.append([i,j,office[i][j]])

dfs(office,0)   #탐색 시작

print(answer)
