from sys import stdin
N = int(input())
M = int(input())
vip = []
seats = []
counts = []
for _ in range(M):
    vip.append(int(stdin.readline().rstrip())-1)

idx = 0
count = 0
if M == 0:
    counts.append(N)
else:
    for i in range(N):
        if i == vip[idx]:
            if count != 0:
                counts.append(count)
                count = 0
            if idx+1 != M:
                idx += 1

        else:
            count += 1
            if i == N-1:
                counts.append(count)

dp = [0] * (N+5)
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, N+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
for item in counts:
    if item != 0:
        answer *= dp[item]

if N == M:
    print(1)
else:
    print(answer)
