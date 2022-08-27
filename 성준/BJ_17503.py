from sys import stdin
input=stdin.readline

def get_heart(val): 
    cnt=0
    tsum=0
    for i in range(K):
        if cnt==N:            #이 때 선호도는 오름차순이므로, cnt==N이면 최대의 선호도이다.
            break
        if bear[i][1] <= val: #간이 버틸 수 있는 도수의 레벨이면
            tsum+=bear[i][0]  #선호도 값을 증가시켜준다.
            cnt+=1
    if cnt < N or tsum < M:   #맥주를 N개를 마실 수 없거나, 선호도를 넘지 못한다면 False
        return False
    return True               #그 외에는 True를 반환

N,M,K=map(int,input().split())
bear=[list(map(int,input().split())) for _ in range(K)]

if sum(sorted(list(zip(*bear))[0],reverse=True)[:N]) < M:   #가장 높은 선호도 N개를 더해도 M을 넘지 못하면 -1
    print(-1)
else:
    left=min(list(zip(*bear))[1])     #도수레벨의 최소값
    right=max(list(zip(*bear))[1])    #도수레벨의 최댓값

    bear.sort(key=lambda x:(-x[0],x[1]))  #배열을 선호도 1.내림차순 2.도수 오름차순으로 정렬
    
    while left<=right:
        mid=(left+right)//2 #간의 레벨의 중간값으로 선언
        if get_heart(mid):  #mid의 값을 통해 선호도를 만족 시킬 수 있으면, 간의 레벨을 더 낮춰본다.
            right=mid-1
        else:               #mid의 값을 통해 선호도를 만족 시킬 수 없으면, 간의 레벨을 높힌다.
            left=mid+1
    print(left)
