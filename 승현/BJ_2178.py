from collections import deque

N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().rstrip(''))))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    dq = deque()
    dq.append((0, 0))
    maps[0][0] = 0
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]

            if ddx >= N or ddx < 0 or ddy >= M or ddy < 0:
                continue
            else:
                if maps[ddx][ddy] == 1:
                    maps[ddx][ddy] = maps[x][y] + 1
                    dq.append((ddx, ddy))

    return maps[N-1][M-1] + 1


print(bfs())
