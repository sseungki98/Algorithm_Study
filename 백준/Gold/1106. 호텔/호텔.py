import sys
MAX_SIZE = sys.maxsize
C, N = map(int, input().split())
price_list= []
for _ in range(N):
    price_list.append(list(map(int, input().split())))

dp = [MAX_SIZE] * (C+100)
dp[0] = 0

for cost, people in price_list:
    for i in range(people, C+100):
        dp[i] = min(dp[i - people]+cost, dp[i])

print(min(dp[C:]))
