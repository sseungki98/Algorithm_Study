N = int(input())
prices = [0] + list(map(int, input().split()))
dp = [0] + [10000001] * N

dp[1] = prices[1]
for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], prices[j] + dp[i-j])


dp[0] = 10000001
print(dp[N])
