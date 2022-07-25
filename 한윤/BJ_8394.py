# 2022-07-25 (월)

import sys

n = int(sys.stdin.readline()) # n : 회의에 참석한 사람의 수
d = [0] * n # dp 테이블 생성

d[0] = 1 # 사람의 수가 1인 경우, 경우의 수는 1개
if n == 1:
    print(d[n - 1])
else:
    d[1] = 2 # 사람의 수가 2인 경우, 경우의 수는 2개
    for i in range(2, n): # 점화식
        d[i] = d[i - 1] + d[i - 2]
        if d[i] >= 10:
            d[i] = d[i] % ((d[i] // 10) * 10) # 끝 자릿수만 저장
    
    print(d[n - 1]) # 정답 출력