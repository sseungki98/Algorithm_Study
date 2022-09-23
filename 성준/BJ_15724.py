import sys
input=sys.stdin.readline

N,M=map(int,input().split())
town=[list(map(int,input().split())) for _ in range(N)]
K=int(input())
dp=[[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):        #부분합을 통해 0,0부터 dp[i][j] 까지의 합을 저장
    for j in range(1,M+1):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]+town[i-1][j-1]-dp[i-1][j-1]

for i in range(K):            #부분합을 통해 해당 영역의 값 계산
    x1,y1,x2,y2=map(int,input().split())
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])
