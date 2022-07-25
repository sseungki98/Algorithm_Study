N=int(input())
dp=[1]*N

if N==1:
    print(dp[0])
else:
    dp[1]=2
    for i in range(2,N):
        dp[i]=(dp[i-1]+dp[i-2])%10  #i번째 사람이 악수를 하는 경우(=i-2번째 사람의 경우의 수) + i번째 사람이 악수를 안하는 경우(=i-1번째 사람의 경우의 수)
    print(dp[N-1])
