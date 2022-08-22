N=int(input())
A=list(map(int,input().split()))
dp=[1]*N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]: #i이전의 j값이 i보다 작으면
            dp[i]=max(dp[i],dp[j]+1)  #해당 구간까지의 dp값에서 +1 더한 것과 현재 dp[i]의 값중 큰 것을 선택한다.
print(max(dp))
