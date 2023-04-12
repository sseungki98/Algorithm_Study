from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(picture, i, j):
    dq = deque()
    dq.appendleft((i, j))
    picture[i][j] = 0
    count = 1
    while dq:
        ddx, ddy = dq.popleft()
        for i in range(4):
            dddx = ddx + dx[i]
            dddy = ddy + dy[i]
            if dddx < 0 or dddx >= n or dddy < 0 or dddy >= m:
                continue

            if picture[dddx][dddy] == 1:
                count += 1
                picture[dddx][dddy] = 0
                dq.appendleft((dddx, dddy))

    return count


n, m = map(int, input().split())
picture = []
count_list = []
for _ in range(n):
    picture.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            count_list.append(bfs(picture, i, j))

print(len(count_list))
if len(count_list) == 0:
    print(0)
else:
    print(max(count_list))