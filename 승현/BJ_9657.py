n = int(input())

dp = [0, 'SK', 'CY', 'SK', 'SK'] + [0] * (n-4)

if n < 5:
    print(dp[n])
else:
    for i in range(5, n+1):
        if dp[i-1] == 'CY' or dp[i-3] == 'CY' or dp[i-4] == 'CY':
            dp[i] = 'SK'
        else:
            dp[i] = 'CY'
    print(dp[n])
