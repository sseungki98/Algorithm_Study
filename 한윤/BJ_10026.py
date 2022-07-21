# 2022-07-22 (금)

from collections import deque

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True # 방문 처리

    graph_value = graph[x][y] # 현재 그래프의 값('R', 'G', 'B' 중 1개)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4): # 좌표 이동
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or nx >= n) or (ny < 0 or ny >= n): # 범위를 벗어나는 경우 무시
                continue

            if graph[nx][ny] == graph_value and not visited[nx][ny]: # 초기 값과 같고, 방문 처리가 되지 않은 경우
                queue.append((nx, ny)) # queue에 삽입
                visited[nx][ny] = True # 방문 처리

n = int(input()) # n x n 크기의 그리드
graph = []
for _ in range(n): # 입력
    graph_temp = list(input())
    graph.append(graph_temp)

normal_count = 0 # 적록색약이 아닌 사람이 본 구역의 수
abnormal_count = 0 # 적록색약인 사람이 본 구역의 수

visited_1 = [[False] * n for _ in range(n)] # 방문처리를 위한 리스트
visited_2 = [[False] * n for _ in range(n)] # 방문처리를 위한 리스트

# (1) 적록색약이 아닌 사람인 경우
for i in range(n):
    for j in range(n):
        if not visited_1[i][j]: # 방문처리가 안된 경우
            bfs(i, j, visited_1)
            normal_count += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G': # 초록색을 빨간색으로 변경
            graph[i][j] = 'R'

# (2) 적록색약의 사람인 경우
for i in range(n):
    for j in range(n):
        if not visited_2[i][j]: # 방문처리가 안된 경우
            bfs(i, j, visited_2)
            abnormal_count += 1

print(normal_count, abnormal_count) # 결과 값 출력