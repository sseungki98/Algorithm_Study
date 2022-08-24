N=int(input())
home=[[0]*N]
for _ in range(N):
    home.append(list(map(int,input().split())))
dp=[[[0]*3 for _ in range(N)] for _ in range(N+1)]
dp[1][1]=[1,0,0]

for i in range(1,N+1):
    for j in range(1,N):
        if i==j==1:   #초기값이 바뀌는 것을 고려
            continue
        if home[i][j]==0:
            dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][2]   #가로의 경우 이 전 위치까지 대각선으로온 경우 + 가로로온 경우
            dp[i][j][1]=dp[i-1][j][1]+dp[i-1][j][2]   #세로의 경우 이 전 위치까지 대각선으로온 경우 + 세로로온 경우
            if home[i-1][j]==0 and home[i][j-1]==0:   #대각선의 경우 주변에 벽이 없고 이 전의 위치에서 가로로온 경우 + 세로로온 경우 + 대각선으로온 경우
                dp[i][j][2]=dp[i-1][j-1][2]+dp[i-1][j-1][0]+dp[i-1][j-1][1]
print(sum(dp[N][N-1]))
