from sys import stdin
N,M=map(int,input().split())
board=[list(map(str,stdin.readline().strip())) for _ in range(N)]   #문자열 입력을 빠르게 받기 위해 readline 으로 입력

rightBoard=[['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]    #옳바른 board의 값

def check(x,y):
    cnt=0
    for i in range(0,8,2):
        if board[x+i]==rightBoard[0]:   #한줄이 같은 경우 다음 줄 진행
            continue
        else: 
            for j in range(8):
                if board[x+i][y+j]!=rightBoard[0][j]:   #같지 않은 값 count
                    cnt+=1
    for i in range(1,8,2):
        if board[x+i]==rightBoard[1]:
            continue
        else:
            for j in range(8):
                if board[x+i][y+j]!=rightBoard[1][j]:
                    cnt+=1
    #변경해야 할 cnt의 갯수 비교
    return min(cnt,64-cnt)  #rightBoard의 순서가 바뀔 수 있는 경우 고려
        
answer=64  #answerdl 8*8을 넘어갈 수 없으므로 최대값을 64로 설정
for i in range(N-7):
    for j in range(M-7):
        answer=min(answer,check(i,j))
print(answer)
