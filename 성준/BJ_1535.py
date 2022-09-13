N=int(input())
health=list(map(int,input().split()))
greed=list(map(int,input().split()))
info=[]
dp=[[0]*100 for _ in range(N+1)]

for h,g in zip(health,greed):
    info.append([h,g])

for i in range(1,N+1):
    for j in range(1,100):
        if j>=info[i-1][0]: dp[i][j]=max(dp[i-1][j],dp[i-1][j-info[i-1][0]]+info[i-1][1]) #남은 체력으로 기쁨을 누릴 수 있는 경우
        else: dp[i][j]=dp[i-1][j]                                                         #그렇지 않은 경우
print(dp[N][99])                                                                          #모두와 악수를 하였을 때, 99의 체력으로 얻을 수 있는 최대 기쁨
