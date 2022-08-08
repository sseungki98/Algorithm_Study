# 2022-08-08 (월)

from collections import deque

def bfs(graph, a, b):
    queue = deque()
    queue.append([a, b])
    graph[b][a] = 0 # 방문 처리는 값을 1에서 0으로 변경시켜 줌으로써 처리

    dx = [-1, 1, 0, 0] # x축으로의 이동 경로
    dy = [0, 0, -1, 1] # y축으로의 이동 경로

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= m or nx < 0 or ny >= n or ny < 0: # 범위를 벗어나는 경우 무시
                continue
            if graph[ny][nx] == 1: # 배추가 있는 경우
                queue.append([nx, ny])
                graph[ny][nx] = 0
    
    return 1

testCount = int(input()) # 테스트 케이스의 개수

for _ in range(testCount):
    # m : 배추밭의 가로 길이, n : 세로 길이, k : 배추가 심어져 있는 위치의 개수
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)] # m x n 크기의 배추 밭 생성
    result = 0 # 최소의 배추흰지렁이 마리 수
    
    for _ in range(k):
        x, y = map(int, input().split()) # 배추의 위치
        graph[y][x] = 1
    
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                result += bfs(graph, i, j)
    
    print(result)