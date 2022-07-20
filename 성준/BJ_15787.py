from sys import stdin

N,M=map(int,stdin.readline().strip().split())
train=[[0]*20 for _ in range(N)]
stack={}  #dictionary 자료구조 사용
answer=0

for i in range(M):
    cmd=list(map(int,stdin.readline().strip().split()))
    if cmd[0]==1: #1번 명령어
        train[cmd[1]-1][cmd[2]-1]=1
    elif cmd[0]==2: #2번 명령어
        train[cmd[1]-1][cmd[2]-1]=0
    elif cmd[0]==3: #3번 명령어
        for k in range(19,0,-1):
            train[cmd[1]-1][k]=train[cmd[1]-1][k-1]
        train[cmd[1]-1][0]=0
    elif cmd[0]==4: #4번 명령어
        for k in range(19):
            train[cmd[1]-1][k]=train[cmd[1]-1][k+1]
        train[cmd[1]-1][19]=0
        
for i in range(N):
    if "".join(map(str,train[i])) in stack: #dictionary 자료 구조를 통해 탐색 시간 단축
        continue
    answer+=1
    stack["".join(map(str,train[i]))]=1 #새로운 형태의 기차라면 stack에 추가
print(answer)
