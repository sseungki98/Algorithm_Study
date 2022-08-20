from sys import stdin
input=stdin.readline

N,K=map(int,input().split())
dp=[0]*(K+1)

for _ in range(N):
    w,v=map(int,input().split())
    for i in range(K,w-1,-1):       #각 무게에 따른 최대값 변경
        dp[i]=max(dp[i],dp[i-w]+v)
print(dp[K])
