N = int(input())

maps = []
visited = [[False] * N for _ in range(N)]
for _ in range(N):
    row = list(map(int, input().split()))
    maps.append(row)

positions = [[0, 0]]
dx = [1, 0]
dy= [0, 1]
while True:
    for position in positions:
        x, y = position[0], position[1]
        if maps[x][y] == -1:
            print("HaruHaru")
            exit(0)

        for i in range(2):
            ddx = position[0] + maps[x][y] * dx[i]
            ddy = position[1] + maps[x][y] * dy[i] # 첫번째 : 우측 이동

            if 0 <= ddx < N and 0 <= ddy < N and visited[ddx][ddy] is False:
                visited[ddx][ddy] = True
                positions.append([ddx, ddy])

    print('Hing')
    break


