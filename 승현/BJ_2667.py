import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(house, a, b):
    n = len(house)
    queue = deque()
    queue.appendleft((a,b))
    house[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft() # 시작 위치 값 꺼내기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if house[nx][ny] == 1:
                house[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


N = int(input())
houses = []
house_count = []

for _ in range(N):
    line = sys.stdin.readline().split()
    houses.append(list(map(int, ''.join(line))))

for i in range(N):
    for j in range(N):
        if houses[i][j] == 1:
            house_count.append(bfs(houses, i, j))

house_count.sort()
print(len(house_count))
for item in house_count:
    print(item)

