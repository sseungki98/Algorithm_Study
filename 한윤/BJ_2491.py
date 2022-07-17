# 2022-06-29 (수)

n = int(input()) # 수열의 길이
arr = list(map(int, input().split())) # 수열
up_max_len = 0 # 증가하는 수열 최대 길이
down_max_len = 0 # 감소하는 수열 최대 길이

''' (이상하게 접근함)
i = 0 # 반복문 변수
while i < n - 1:
    idx = 0 # 인덱스 저장
    current_len = 1 # 현재 길이
    same_flag = 0 # (3) 같은 숫자인 경우, flag 값이 1을 가짐
    same_cnt = 0 # 안쪽 반복문에서 같은 수를 처음 만난 경우, flag 값이 1을 가짐
    if arr[i] > arr[i + 1]: # (1) 연속해서 작아지는 수열인 경우
        current_len += 1
        i += 1
        while i < n - 1:
            if arr[i] < arr[i + 1]: # 반복문 탈출 조건
                break
            if same_cnt == 0 and arr[i] == arr[i + 1]: # 같은 수인 경우, 시작 인덱스를 기억해야 함
                same_cnt = 1
                idx = i
            current_len += 1
            i += 1
    elif arr[i] < arr[i + 1]: # (2) 연속해서 커지는 수열인 경우
        current_len += 1
        i += 1
        while i < n - 1:
            if arr[i] > arr[i + 1]: # 반복문 탈출 조건
                break
            if same_cnt == 0 and arr[i] == arr[i + 1]: # 같은 수인 경우, 시작 인덱스를 기억해야 함
                same_cnt = 1
                idx = i
            current_len += 1
            i += 1
    else: # (3) 같은 숫자인 경우
        same_flag = 1
        current_len += 1
        i += 1
    
    if same_flag == 0 and max_len < current_len: # 최대 길이 값을 갱신
        max_len = current_len
    
    if idx: # 인덱스 값이 존재하는 경우
        i = idx # i값을 변경
print(max_len)
'''
max_len = 1 # 임시적으로 저장하는 길이 변수
for i in range(n - 1): # 증가하는 수열인 경우
    if arr[i] <= arr[i + 1]:
        max_len += 1
    else:
        up_max_len = max(up_max_len, max_len)
        max_len = 1

up_max_len = max(up_max_len, max_len) # 반복문이 끝난 후의 최댓값 갱신

max_len = 1 # 임적으로 저장하는 길이 변수
for i in range(n - 1): # 감소하는 수열인 경우
    if arr[i] >= arr[i + 1]:
        max_len += 1
    else:
        down_max_len = max(down_max_len, max_len)
        max_len = 1

down_max_len = max(down_max_len, max_len) # 반복문이 끝난 후의 최댓값 갱신

print(max(up_max_len, down_max_len))