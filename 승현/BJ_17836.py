from collections import deque

mx = [0, 0, 1, -1]
my = [1, -1, 0, 0]
N, M, T = map(int, input().split())
maps = []
for _ in range(N):
    line = list(map(int, input().split()))
    for k in range(len(line)):
        if line[k] == 2:
            line[k] = 'X'
    maps.append(line)


def bfs():
    dq = deque()
    dq.append((0, 0))
    maps[0][0] = 1
    sword_count = 10001

    while dq:
        dx, dy = dq.popleft()
        for i in range(4):
            ddx = dx + mx[i]
            ddy = dy + my[i]
            if ddx >= N or ddx < 0 or ddy >= M or ddy < 0:
                continue
            else:
                if maps[ddx][ddy] == 0:
                    maps[ddx][ddy] = maps[dx][dy] + 1
                    dq.append((ddx, ddy))

                elif maps[ddx][ddy] == 'X':
                    sword_count = maps[dx][dy] + (M-1-ddy) + (N-1-ddx)
                    maps[ddx][ddy] = maps[dx][dy] + 1
                    dq.append((ddx, ddy))

    if maps[N-1][M-1] == 0:
        if sword_count <= T:
            return sword_count
        else:
            return 'Fail'
    else:
        maps[N-1][M-1] = maps[N-1][M-1] - 1
        if maps[N-1][M-1] >= sword_count and sword_count <= T:
            return sword_count
        elif maps[N-1][M-1] <= sword_count and maps[N-1][M-1] <= T:
            return maps[N-1][M-1]
        else:
            return 'Fail'




print(bfs())






