from sys import stdin

N=int(stdin.readline())
budgets=list(map(int,stdin.readline().split()))
max_budget=int(stdin.readline())

left=1
right=max(budgets)
answer=0

while left<=right:
    mid=(left+right)//2     #예산 상한선 설정
    total=0
    
    for budget in budgets:
        if budget <= mid:   #상한선 이하금액이면 그대로 total에 더한다.
            total+=budget
        else:               #그렇지 않은경우 상한선 금액을 더한다.
            total+=mid
    if total>max_budget:    #총 비용이 예산 초과라면 상한선을 줄인다.
        right=mid-1
    else:                   #예산이 남는다면 상한선을 늘린다.
        left=mid+1
print(left-1) #최대 상한선을 출력한다.
