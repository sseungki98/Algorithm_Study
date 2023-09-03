N = int(input())  # N = 5

store = []
dp = []
for i in range(N):
    store.append(list(map(int, input().split())))
    dp.append([0] * (i+1))

dp[0][0] = store[0][0]

for i in range(N-1):
    for j in range(len(store[i])):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + store[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + store[i+1][j+1])

print(max(dp[N-1]))



