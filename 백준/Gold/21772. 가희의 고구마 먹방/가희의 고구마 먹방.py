R, C, T = map(int, input().split())
maps = []
potato = [0]
start_x, start_y = 0, 0
for _ in range(R):
    maps.append(list(input()))

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'G':
            start_x, start_y = i, j


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(start_i: int, start_j: int, ate: int, time: int):
    if time == T:
        if maps[start_i][start_j] == 'S':
            potato.append(ate+1)
            return
        else:
            potato.append(ate)
            return
    for k in range(4):
        ddx = start_i + dx[k]
        ddy = start_j + dy[k]
        if ddx < 0 or ddx >= R or ddy < 0 or ddy >= C:
            continue
        else:
            if maps[ddx][ddy] == '#':
                continue
            elif maps[ddx][ddy] == 'S':
                maps[ddx][ddy] = '.'
                dfs(ddx, ddy, ate+1, time+1)
                maps[ddx][ddy] = 'S'
            else:
                dfs(ddx, ddy, ate, time+1)


dfs(start_x, start_y, 0, 0)
print(max(potato))




