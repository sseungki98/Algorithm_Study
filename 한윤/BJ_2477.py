# 2022-07-14 (목)

n = int(input()) # n : 1m^2의 넓이에 자라는 참외의 개수

graph_row = [] # 가로에 해당하는 참외 밭 부분
graph_column = [] # 세로에 해당하는 참외 밭 부분

# 북, 남, 서, 동 (가장 큰 변의 방향인 경우 1)
n_flag = 0
s_flag = 0
w_flag = 0
e_flag = 0

for _ in range(6): # 육각형의 참외 밭 입력
    # d : 변의 방향(1 : 동쪽, 2 : 서쪽, 3 : 남쪽, 4 : 북쪽), l : 변의 길이
    d, l = map(int, input().split())

    if d == 1 or d == 2: # 가로 부분인 경우
        graph_row.append([d, l])
    else: # 세로 부분인 경우
        graph_column.append([d, l])

# 큰 사각형의 가로, 세로
big_row = max(x[1] for x in graph_row)
big_column = max(x[1] for x in graph_column)

# 큰 사각형의 가로, 세로 인덱스
row_idx = 0
column_idx = 0

# 작은 사각형의 가로, 세로
small_row = 0
small_column = 0

for i in range(3): # 인덱스 찾기
    if graph_row[i][1] == big_row:
        row_idx = i
        if graph_row[i][0] == 1:
            e_flag = 1
        else:
            w_flag = 1
    if graph_column[i][1] == big_column:
        column_idx = i
        if graph_column[i][0] == 3:
            s_flag = 1
        else:
            n_flag = 1
    
if n_flag == 1 and w_flag == 1: # 가장 큰 변의 방항이 북쪽과 서쪽인 경우
    small_row = graph_row[(row_idx + 1) % 3][1]
    small_column = graph_column[(column_idx + 2) % 3][1]
elif n_flag == 1 and e_flag == 1: # 가장 큰 변의 방향이 북쪽과 동쪽인 경우
    small_row = graph_row[(row_idx + 2) % 3][1]
    small_column = graph_column[(column_idx + 1) % 3][1]
elif s_flag == 1 and w_flag == 1: # 가장 큰 변의 방향이 남쪽과 서쪽인 경우
    small_row = graph_row[(row_idx + 2) % 3][1]
    small_column = graph_column[(column_idx + 1) % 3][1]
else: # 가장 큰 변의 방향이 남쪽과 동쪽인 경우
    small_row = graph_row[(row_idx + 1) % 3][1]
    small_column = graph_column[(column_idx + 2) % 3][1]

result = (big_row * big_column) - (small_row * small_column) # 참외 밭의 넓이 계산

print(result * n)