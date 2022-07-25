# 2022-07-25 (월)

# m : 가로의 길이, n : 세로의 길이
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(input())) # m x n 크기의 보드 입력

graph_b = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'] # Black으로 시작하는 행
graph_w = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'] # White로 시작하는 행

min_square_count = n * m # 다시 칠해야 하는 정사각형 개수의 최솟값 (보드의 크기로 초기화)

# 전체 탐색
for i in range(n - 7):
    for j in range(m - 7):
        # i, j를 기준으로 8 x 8크기의 체스판 확인

        b_square_count = 0 # 현재 체스판에서 다시 칠해야 하는 정사각형의 개수 (시작점 Black)
        w_square_count = 0 # 현재 체스판에서 다시 칠해야 하는 정사각형의 개수 (시작점 White)
        
        # 홀수, 짝수 행을 구분하는 플래그 값
        n_flag = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if n_flag == 0: # Black으로 시작하는 행의 경우
                    if graph[x][y] != graph_b[y - j]: # 해당 행이 일치하지 않는 경우
                        b_square_count += 1
                else: # White으로 시작하는 행의 경우
                    if graph[x][y] != graph_w[y - j]: # 해당 행이 일치하지 않는 경우
                        b_square_count += 1
            # 플래그 값 변경
            if n_flag == 0:
                n_flag = 1
            else:
                n_flag = 0
        
        # 홀수, 짝수 행을 구분하는 플래그 값
        n_flag = 1
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if n_flag == 0: # Black으로 시작하는 행의 경우
                    if graph[x][y] != graph_b[y - j]: # 해당 행이 일치하지 않는 경우
                        w_square_count += 1
                else: # White으로 시작하는 행의 경우
                    if graph[x][y] != graph_w[y - j]: # 해당 행이 일치하지 않는 경우
                        w_square_count += 1
            # 플래그 값 변경
            if n_flag == 0:
                n_flag = 1
            else:
                n_flag = 0
        
        # 현재 구한 값이 더 작은 경우 최솟값 갱신
        if min_square_count > min(b_square_count, w_square_count):
            min_square_count = min(b_square_count, w_square_count)

print(min_square_count)