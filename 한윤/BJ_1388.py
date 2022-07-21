# 2022-07-21 (목)

# n : 방 바닥의 세로 크기, m : 방 바닥의 가로 크기
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph_temp = list(input())
    graph.append(graph_temp)

wood_count = 0 # 필요한 나무 판자의 개수

# '-' (가로 부분) 체크
for i in range(n):
    row_flag = 0 # 가로 부분의 연속된 부분을 확인하기 위해 사용하는 변수
    for j in range(m):
        if row_flag == 0 and graph[i][j] == '-':
            row_flag = 1
        elif row_flag == 1 and graph[i][j] == '-':
            continue
        elif row_flag == 1 and graph[i][j] != '-':
            row_flag = 0
            wood_count += 1
    if row_flag == 1: # 나머지 처리
        wood_count += 1

# '|' (세로 부분) 체크
for i in range(m):
    column_flag = 0 # 세로 부분의 연속된 부분을 확인하기 위해 사용하는 변수
    for j in range(n):
        if column_flag == 0 and graph[j][i] == '|':
            column_flag = 1
        elif column_flag == 1 and graph[j][i] == '|':
            continue
        elif column_flag == 1 and graph[j][i] != '|':
            column_flag = 0
            wood_count += 1
    if column_flag == 1: # 나머지 처리
        wood_count += 1

print(wood_count)