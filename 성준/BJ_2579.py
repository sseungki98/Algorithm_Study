N=int(input())
stairs=[int(input()) for _ in range(N)]

if N < 3:
    print(sum(stairs))
else:  
    dp=[0]*N
    dp[0]=stairs[0]
    dp[1]=stairs[0]+stairs[1]
    dp[2]=max(stairs[0]+stairs[2],stairs[1]+stairs[2])  #현재 계단을 밟아야 하므로 이전 계단과 전전계단 비교
    
    for i in range(3,N):
        dp[i]=max(dp[i-2]+stairs[i],dp[i-3]+stairs[i]+stairs[i-1])  #이 전 계단에서 오는 경우와 전전계단에서 바로 오는 경우 비교
    print(dp[N-1])
