N = int(input())

# count = 0
# def stair_num(num):
#     global count
#     if len(num) == N:
#         count += 1
#         return
#
#     if int(num[-1]) + 1 != 10:
#         stair_num(num + str(int(num[-1]) + 1))
#
#     if int(num[-1]) - 1 != -1:
#         stair_num(num + str(int(num[-1]) - 1))
#
#     return
#
#
# for i in range(9):
#     stair_num(str(i+1))
#
# print(count)

dp = [[0] * 10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif 1 <= j <= 8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]

print(sum(dp[N]) % 1000000000)
