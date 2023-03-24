board = list(map(int, input().split()))
N = board[0]
M = board[1]

candys = []
dp = [[0] * M for _ in range(N)]
for _ in range(N):
    candys.append(list(map(int, input().split())))

f_sum = 0
for i in range(M):
    f_sum += candys[0][i]
    dp[0][i] = f_sum

ff_sum = 0
for i in range(len(candys)):
    ff_sum += candys[i][0]
    dp[i][0] = ff_sum

for i in range(N-1):
    for j in range(M-1):
        if dp[i][j+1] >= dp[i+1][j]:
            dp[i+1][j+1] = dp[i][j+1] + candys[i+1][j+1]
        else:
            dp[i+1][j+1] = dp[i+1][j] + candys[i+1][j+1]

print(dp[N-1][M-1])