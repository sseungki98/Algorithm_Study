dx = [0 ,0 ,1, -1]
dy= [1, -1, 0, 0]
R, C = map(int, input().split())
maps = []
maps.append(['.']*(C+2))
for _ in range(R):
    line = ['.'] + list(map(str, input().rstrip(''))) + ['.']
    maps.append(line)
maps.append(['.']*(C+2))

for i in range(1,R+1):
    for j in range(1,C+1):
        if maps[i][j] == 'X':
            ocean_count = 0
            for k in range(4):
                mx = i + dx[k]
                my = j + dy[k]
                if maps[mx][my] == '.':
                    ocean_count += 1
            if ocean_count == 3 or ocean_count == 4:
                maps[i][j] = 'O'
min_j = C+2
max_j = -1
min_i = R+2
max_i = -1


for i in range(1,R+1):
    for j in range(1,C+1):
        if maps[i][j] == 'O':
            maps[i][j] = '.'
        elif maps[i][j] == 'X':
            min_j = min(min_j, j)
            max_j = max(max_j, j)
            min_i = min(min_i, i)
            max_i = max(max_i, i)

for i in range(min_i, max_i+1):
    for j in range(min_j, max_j+1):
        print(maps[i][j], end='')
    print('')

