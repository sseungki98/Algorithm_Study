# 주어진 길이 N에 대한 오르막 수의 개수를 구하는 프로그램
N = int(input())
dp = [[1 for _ in range(10)] for _ in range(N)]

if N == 1:
    print(10)
else:
    for i in range(1, N):
        for j in range(9, -1, -1):
            count = 0
            for k in range(9, -1, -1):
                if j >= k:
                    count += dp[i-1][k]
            dp[i][j] = count

    print(sum(dp[N-1]) % 10007)
