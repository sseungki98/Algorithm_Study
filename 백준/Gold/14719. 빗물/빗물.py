N, M = map(int, input().split())
blocks = list(map(int, input().split()))
maps = [[0 for _ in range(N)] for _ in range(M)]
rains = 0

for i in range(M):
    for j in range(blocks[i]):
        maps[i][j] = 1

for i in range(N):
    flag = False
    temp_count = 0
    zero_flag = False
    for j in range(M):
        if maps[j][i] == 0:
            if not flag:
                if j == 0:
                    zero_flag = True
                flag = True
                temp_count += 1
            else:
                temp_count += 1
                continue
        else:
            if flag and not zero_flag:
                rains += temp_count
                temp_count = 0
                flag = False
            else:
                flag = False
                zero_flag = False
                temp_count = 0
print(rains)
