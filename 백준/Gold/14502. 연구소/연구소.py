from itertools import combinations
from collections import deque
import copy
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(start_i, start_j, t_map):
    dq = deque()
    dq.append((start_i, start_j))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0<=ddx<N and 0<=ddy<M:
                if t_map[ddx][ddy] == 0:
                    t_map[ddx][ddy] = 2
                    dq.append((ddx, ddy))

N, M = map(int, input().split())
maps = []
answer = -1
for _ in range(N):
    maps.append(list(map(int, input().split())))

index_list = []
virus_index_list = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            index_list.append([i, j])
        elif maps[i][j] == 2:
            virus_index_list.append([i, j])

combi_list = list(combinations(index_list, 3))
for item in combi_list:
    count = 0
    temp_list = copy.deepcopy(maps)
    for idx in item:
        temp_list[idx[0]][idx[1]] = 1

    for idx in virus_index_list:
        bfs(idx[0], idx[1], temp_list)

    for n in range(N):
        for m in range(M):
            if temp_list[n][m] == 0:
                count += 1

    answer = max(answer, count)

print(answer)




