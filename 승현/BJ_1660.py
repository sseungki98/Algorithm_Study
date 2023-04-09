import sys

balls = []
num_sum = 0

N = int(input())

for i in range(1, 300000):
    num_sum += (i*(i+1))//2
    balls.append(num_sum)

    if num_sum > N:
        break

dp = [sys.maxsize] * (N+1)

for i in range(1, N+1):
    for ball in balls:
        if ball == i:
            dp[i] = 1
            break
        elif ball > i:
            break

        dp[i] = min(dp[i], 1 + dp[i-ball])

print(dp[N])