# 2022-07-08 (금)

import copy

n = int(input()) # n : 보드의 크기
data = []
for _ in range(n):
    # 보드에 채워져 있는 사탕의 색상 입력 (C : 빨간색, P : 파란색, Z : 초록색, Y : 노란색)
    data.append(list(input()))

max_candy = 0 # 상근이가 먹을 수 있는 사탕의 최대 개수

# (1) 가로로 사탕의 색이 다른 인접한 두 칸을 선택 => 세로의 최대 개수 확인
for i in range(n):
    for j in range(n - 1):
        if data[i][j] != data[i][j + 1]:
            data[i][j], data[i][j + 1] = data[i][j + 1], data[i][j] # swap
            
            # 가로 부분의 연속된 개수 체크
            for x in range(n):
                temp = data[x][0] # 첫 번째 원소를 기준으로 저장
                sum_candy = 1 # 연속된 사탕의 개수를 저장하는 변수
                for y in range(1, n):
                    if temp == data[x][y]: # 위에서 저장한 값과 같은 값인 경우
                        sum_candy += 1
                    else: # 위에서 저장한 값과 다른 값인 경우
                        if max_candy < sum_candy: # 최댓값 변경
                            max_candy = sum_candy
                            temp = data[x][y]
                            sum_candy = 1
                        else:
                            temp = data[x][y]
                            sum_candy = 1
                
                if max_candy < sum_candy: # 최댓값 변경
                    max_candy = sum_candy

            # 세로 부분의 연속된 개수 체크
            for x in range(n):
                temp = data[0][x] # 첫 번째 원소를 기준으로 저장
                sum_candy = 1 # 연속된 사탕의 개수를 저장하는 변수
                for y in range(1, n):
                    if temp == data[y][x]: # 위에서 저장한 값과 같은 값인 경우
                        sum_candy += 1
                    else: # 위에서 저장한 값과 다른 값인 경우
                        if max_candy < sum_candy: # 최댓값 변경
                            max_candy = sum_candy
                            temp = data[y][x]
                            sum_candy = 1
                        else:
                            temp = data[y][x]
                            sum_candy = 1
                
                if max_candy < sum_candy: # 최댓값 변경
                    max_candy = sum_candy
            
            data[i][j], data[i][j + 1] = data[i][j + 1], data[i][j] # swap (원상태)

# (2) 세로로 사탕의 색이 다른 인접한 두 칸을 선택 => 가로의 최대 개수 확인
for i in range(n):
    for j in range(n - 1):
        if data[j][i] != data[j + 1][i]:
            data[j][i], data[j + 1][i] = data[j + 1][i], data[j][i] # swap
            
            # 가로 부분의 연속된 개수 체크
            for x in range(n):
                temp = data[x][0] # 첫 번째 원소를 기준으로 저장
                sum_candy = 1 # 연속된 사탕의 개수를 저장하는 변수
                for y in range(1, n):
                    if temp == data[x][y]: # 위에서 저장한 값과 같은 값인 경우
                        sum_candy += 1
                    else: # 위에서 저장한 값과 다른 값인 경우
                        if max_candy < sum_candy: # 최댓값 변경
                            max_candy = sum_candy
                            temp = data[x][y]
                            sum_candy = 1
                        else:
                            temp = data[x][y]
                            sum_candy = 1
                
                if max_candy < sum_candy: # 최댓값 변경
                    max_candy = sum_candy
            
            # 세로 부분의 연속된 개수 체크
            for x in range(n):
                temp = data[0][x] # 첫 번째 원소를 기준으로 저장
                sum_candy = 1 # 연속된 사탕의 개수를 저장하는 변수
                for y in range(1, n):
                    if temp == data[y][x]: # 위에서 저장한 값과 같은 값인 경우
                        sum_candy += 1
                    else: # 위에서 저장한 값과 다른 값인 경우
                        if max_candy < sum_candy: # 최댓값 변경
                            max_candy = sum_candy
                            temp = data[y][x]
                            sum_candy = 1
                        else:
                            temp = data[y][x]
                            sum_candy = 1
                
                if max_candy < sum_candy: # 최댓값 변경
                    max_candy = sum_candy

            data[j][i], data[j + 1][i] = data[j + 1][i], data[j][i] # swap (원상태)

print(max_candy) # 상근이가 먹을 수 있는 사탕의 최대 개수를 출력