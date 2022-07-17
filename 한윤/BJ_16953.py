# 2022-07-15 (금)

import sys

# a, b의 범위 : 1 <= a < b <= 10^9
a, b = map(int, sys.stdin.readline().split())
equal_ab = 0 # a를 b로 만들 수 있는 지 체크하는 변수
count = 0 # a를 b로 바꾸는데 필요한 연산의 횟수

while a < b:
    if b % 2 == 1: # b가 2로 나누어 떨어지지 않는 경우
        # 1을 수의 가장 오른쪽에서 제거하는 작업
        b -= 1
        if b % 10 != 0: # 1로 끝나는 수가 아닌 홀수의 경우는 만들 수 없는 수인 경우이다.
            break
        b //= 10

        # 연산 횟수 count
        count += 1

    else: # b가 2로 나누어 떨어지는 경우
        # 2를 나누는 작업
        b //= 2

        # 연산 횟수 count
        count += 1
    
    if a == b:
        equal_ab = 1 # 플래그 값 변경
        break

if equal_ab == 1:
    print(count + 1) # 출력 시, a를 b로 바꾸는데 필요한 연산의 최솟값에 1을 더하여 출력
else:
    print(-1)