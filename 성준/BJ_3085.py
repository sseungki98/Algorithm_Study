from sys import stdin
import copy

dx=[-1,0,1,0]
dy=[0,1,0,-1]

N=int(input())
candy=[list(map(str,stdin.readline().strip())) for _ in range(N)]
answer=0

def find(x,y,tmp):  #x번째 행과 y번째 열에서 길이가 가장 긴 candy를 찾는 함수
    global answer
    count=1
    for i in range(N-1):
        if tmp[x][i]==tmp[x][i+1]:
           count+=1 
        else:
            if count > answer:
                answer=count
            count=1
    if count > answer:
        answer=count
    count=1
    for i in range(N-1):
        if tmp[i][y]==tmp[i+1][y]:
            count+=1 
        else:
            if count > answer:
                answer=count
            count=1
    if count > answer:
        answer=count
        
def change(x,y,tmp):
    find(x,y,tmp) #현재 주어진 값의 x,y 탐색
    tp=tmp[x][y]  #수정 전 값 유지
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and tmp[x][y]!=tmp[nx][ny]:  #유효한 인접한 값중 값이 다른 경우 값을 서로 변경
            tmp[x][y]=tmp[nx][ny]
            tmp[nx][ny]=tp
            find(nx,ny,tmp) #값이 변경된 nx,ny 탐색
            tmp[nx][ny]=tmp[x][y] #탐색 후 원상 복구
            tmp[x][y]=tp
            
for i in range(N):
    for j in range(N):
        temp=copy.deepcopy(candy)
        change(i,j,temp)  #i,j를 기준으로 상하좌우 탐색
        
print(answer)
