from sys import stdin
input=stdin.readline

N=int(input())
grape=[int(input()) for _ in range(N)]
dp=[0]*N

if N==1:
    print(grape[0])
elif N==2:
    print(grape[0]+grape[1])
else:
    dp[0]=grape[0]
    dp[1]=grape[0]+grape[1]
    dp[2]=max(dp[1],grape[2]+grape[0],grape[1]+grape[2])
    for i in range(3,N):  #i번째 잔을 마시지 않는 경우 vs i번째 잔과 i-1번째 잔을 같이 마시는 경우 vs i번째 잔과 i-2번째 잔을 같이 마시는 경우
        dp[i]=max(dp[i-1],grape[i]+grape[i-1]+dp[i-3],grape[i]+dp[i-2])
    print(dp[N-1])
