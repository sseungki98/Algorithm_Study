N=int(input())
num_list=list(map(int,input().split()))
dp_up=[1]*N
dp_down=[1]*N

for i in range(1,N):    #앞의 값과 비교하여 연속되는 수열은 앞의 값에 +1을 하여 이어준다.
    if num_list[i]>=num_list[i-1]:  #연속해서 커지는 수열
        dp_up[i]=dp_up[i-1]+1
    if num_list[i]<=num_list[i-1]:  #연속해서 감소하는 수열
        dp_down[i]=dp_down[i-1]+1
            
print(max(max(dp_up),max(dp_down))) #감소하는 수열과 증가하는 수열 중 큰 값
