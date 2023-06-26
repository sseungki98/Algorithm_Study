from collections import deque
M, N = map(int, input().split())
board = []
for _ in range(M):
    board.append(list(map(int, input()))) # 0=> white, 1=> black

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i,j):
    dq = deque()
    dq.append((i,j))
    board[i][j] = 2
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            ddx = x + dx[k]
            ddy = y + dy[k]
            if ddx<0 or ddx>=M or ddy<0 or ddy>=N:
                continue
            else:
                if board[ddx][ddy] == 1 or board[ddx][ddy] == 2:
                    continue
                else:
                    board[ddx][ddy] = 2
                    dq.append((ddx, ddy))


def dfs(i,j):
    board[i][j] = 2
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0<=x<M and 0<=y<N and board[x][y] == 0:
            dfs(x,y)

for i in range(N):
    if board[0][i] == 0:
        bfs(0,i)

for item in board[M-1]:
    if item == 2:
        print('YES')
        exit()
print('NO')
