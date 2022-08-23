# 2022-08-23 (화)

n = int(input()) # n : 수열 A의 크기
arr = list(map(int, input().split())) # 수열 A

d = [1] * n # dp 테이블 생성

# LIS(Longest Increasing Subsequence) 알고리즘
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] < arr[j]:
            # 기존 dp 테이블 값과, 현재 값에 더한 값 중 최댓값으로 갱신
            d[j] = max(d[i] + 1, d[j])

print(max(d)) # dp 테이블 중 최댓값 출력