# 2022-07-25 (월)

'''
from bisect import bisect_left, bisect_right

n = int(input()) # n : 색을 칠해야 하는 문제의 수
words = list(input()) # n개의 문자 (R : 빨간색, B : 파란색)
count = 0 # 필요한 작업 횟수의 최솟값

r_cnt = words.count('R') # 빨간색 문제의 수
b_cnt = words.count('B') # 파란색 문제의 수

if r_cnt > b_cnt: # 빨간색 문제가 파란색 문제보다 많은 경우
    left_idx = bisect_left(words, 'R') # 빨간색의 시작 위치
    right_idx = bisect_right(words, 'R') - 1 # 빨간색의 종료 위치

    if left_idx == 0:
        count += 1 # left_idx와 right_idx를 전부 빨간색으로 칠하는 과정
        for i in range(right_idx): # 파란색만 따로 칠하는 과정
            if words[i] == 'B':
                count += 1
        
        if right_idx != n: # right_idx가 끝 부분이 아닌 경우
            count += 1 # 파란색을 칠하는 횟수 추가
    else: 
        temp = words[0] # 시작 부분
        count += 1

        if left_idx == 1:
            if temp != words[1]:
                count += 1
        else:
            for i in range(1, left_idx): # 시작 부분부터 left_idx부분 까지의 작업
                if words[i] != temp:
                    count += 1
                    temp = words[i]

        for i in range(left_idx, right_idx): # left_idx와 right_idx를 전부 빨간색으로 칠한 뒤, 파란색만 따로 칠하는 과정
            if words[i] == 'B':
                count += 1

        if right_idx < (n - 1): # right_idx가 끝 부분이 아닌 경우
            count += 1 # 파란색을 칠하는 횟수 추가

else: # 파란색 문제가 빨간색 문제보다 많은 경우
    left_idx = bisect_left(words, 'B') # 파란색의 시작 위치
    right_idx = bisect_right(words, 'B') # 파란색의 종료 위치

    print(left_idx)
    print(right_idx)

    if left_idx == 0:
        count += 1 # left_idx와 right_idx를 전부 파란색으로 칠하는 과정
        for i in range(right_idx): # 빨간색만 따로 칠하는 과정
            if words[i] == 'R':
                count += 1

        if right_idx != n: # right_idx가 끝 부분이 아닌 경우
            count += 1 # 빨간색을 칠하는 횟수 추가
    else: 
        temp = words[0] # 시작 부분
        count += 1

        if left_idx == 1:
            if temp != words[1]:
                count += 1
        else:
            for i in range(1, left_idx): # 시작 부분부터 left_idx부분 까지의 작업
                if words[i] != temp:
                    count += 1
                    temp = words[i]

        for i in range(left_idx, right_idx): # left_idx와 right_idx를 전부 빨간색으로 칠한 뒤, 파란색만 따로 칠하는 과정
            if words[i] == 'R':
                count += 1

        if right_idx < (n - 1): # right_idx가 끝 부분이 아닌 경우
            count += 1 # 빨간색을 칠하는 횟수 추가

print(count) # 최소한의 작업 횟수 출력
'''

n = int(input()) # n : 색을 칠해야 하는 문제의 수
n_count = 1 # 필요한 작업 횟수 (아래의 start와 end부분을 칠했다고 가정)
words = list(input())

x = words[0] # 시작 부분의 색을 저장
words_start = 0 # 시작 부분의 인덱스를 저장
words_end = 0 # 끝 부분의 인덱스를 저장
for i in range(n - 1, -1, -1):
    if words[i] == x:
        words_end = i
        break
words_flag = 0 # 다른 색의 연속된 부분을 체크하기 위한 플래그 값

for i in range(words_start + 1, words_end + 1): # start와 end 인덱스 사이의 다른 색이 있는 경우 count
    if words_flag == 0 and words[i] != x: # 플래그 값이 0이고, 다른 색을 만난 경우
        words_flag = 1
    elif words_flag == 1 and words[i] == x: # 플래그 값이 1이고, 같은 색을 만난 경우
        words_flag = 0
        n_count += 1

if words_end != (n - 1): # 마지막 인덱스가 아닌 경우, 뒤의 다른 색이 있으므로 count 추가
    n_count += 1

print(n_count) # 최소한의 작업 횟수 출력

# 처음 코딩을 할 때, 문제의 수가 더 많은 색에 따라 경우의 수가 달라질 것이라고 생각함.
# 문제의 수에 관계없이, 경우의 수는 동일하므로 시작 지점의 색의 인덱스와 그 색의 끝 인덱스를 찾고, 사이의 다른 색의 개수와 마지막 부분의 처리를 하면 경우의 수가 갖춰짐.

# + (문제 해설)
# 위 문제는 그리디 문제이다.
# 모든 문제를 빨간색 혹은 파란색으로 칠한 뒤, 나머지 색으로 칠한 경우 중 최소가 되는 값을 선택하면 된다.