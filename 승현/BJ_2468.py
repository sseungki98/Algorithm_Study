from sys import stdin
from collections import deque
N = int(input())
maps = []
rain_nums = set()
rain_nums.add(0)
for _ in range(N):
    input_line = list(map(int, stdin.readline().split()))
    maps.append(input_line)
    for item in input_line:
        rain_nums.add(item)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(rain_maps, i, j):
    dq = deque()
    dq.append((i, j))
    rain_maps[i][j] = 1

    while dq:
        x, y = dq.popleft()
        for k in range(4):
            ddx = x + dx[k]
            ddy = y + dy[k]
            if ddx >= N or ddx < 0 or ddy >= N or ddy < 0:
                continue
            else:
                if rain_maps[ddx][ddy] == 0:
                    dq.append((ddx, ddy))
                    rain_maps[ddx][ddy] = 1

    return


safe_count = []
for item in rain_nums:
    rain_maps = []
    for i in range(N):
        row = []
        for a in maps[i]:
            if a <= item:
                row.append(1)
            else:
                row.append(0)
        rain_maps.append(row)

    ct = 0
    for i in range(N):
        for j in range(N):
            if rain_maps[i][j] == 0:
                bfs(rain_maps, i, j)
                ct += 1

    safe_count.append(ct)

print(max(safe_count))




