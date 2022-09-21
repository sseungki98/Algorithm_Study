N=int(input())
card=[0]+list(map(int,input().split()))
dp=[False for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i+1):
        if not dp[i]: dp[i]=dp[i-j]+card[j]
        else: dp[i]=min(dp[i],dp[i-j]+card[j])
print(dp[N])
