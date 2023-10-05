from collections import deque
M, N, K = map(int, input().split())
route = [[0 for _ in range(N)] for _ in range(M)]
answer = []
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            route[i][j] = 1


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(_i: int, _j: int) -> int:
    dq = deque()
    dq.append((_i, _j))
    route[_i][_j] = 1
    count = 0
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            ddx = x + dx[k]
            ddy = y + dy[k]
            if ddx > M-1 or ddx < 0 or ddy > N-1 or ddy < 0:
                continue
            else:
                if route[ddx][ddy] == 0:
                    count += 1
                    route[ddx][ddy] = 1
                    dq.append((ddx, ddy))

    return count


for i in range(M):
    for j in range(N):
        if route[i][j] == 0:
            answer.append(bfs(i, j)+1)

print(len(answer))
print(*sorted(answer))