from collections import deque
N = int(input())
maps = []
visited = [[False for _ in range(N)] for _ in range(N)]
rg_visited = [[False for _ in range(N)] for _ in range(N)]
count = 0
rg_count = 0
for _ in range(N):
    maps.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(a, b):
    if visited[a][b] is False:
        dq = deque()
        dq.append((a, b))
        temp_count = 1
        visited[a][b] = True
        while dq:
            x, y = dq.popleft()
            for k in range(4):
                ddx = x + dx[k]
                ddy = y + dy[k]
                if ddx >= N or ddx < 0 or ddy >= N or ddy < 0:
                    continue
                else:
                    if visited[ddx][ddy]:
                        continue
                    else:
                        if maps[x][y] == maps[ddx][ddy]:
                            dq.append((ddx, ddy))
                            visited[ddx][ddy] = True
                            temp_count += 1

        return temp_count


def rgdfs(a, b):
    if rg_visited[a][b] is False:
        dq = deque()
        dq.append((a, b))
        temp_count = 1
        rg_visited[a][b] = True
        while dq:
            x, y = dq.popleft()
            for k in range(4):
                ddx = x + dx[k]
                ddy = y + dy[k]
                if ddx >= N or ddx < 0 or ddy >= N or ddy < 0:
                    continue
                else:
                    if rg_visited[ddx][ddy]:
                        continue
                    else:
                        if maps[x][y] == maps[ddx][ddy]:
                            dq.append((ddx, ddy))
                            rg_visited[ddx][ddy] = True
                            temp_count += 1
                        if (maps[x][y] == 'R' or maps[x][y] == 'G') and (maps[ddx][ddy] == 'R' or maps[ddx][ddy] == 'G'):
                            dq.append((ddx, ddy))
                            rg_visited[ddx][ddy] = True
                            temp_count += 1

        return temp_count


for i in range(N):
    for j in range(N):
        if dfs(i, j) is not None:
            count += 1
        if rgdfs(i, j) is not None:
            rg_count += 1

print(count, rg_count)



