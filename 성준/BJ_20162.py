N=int(input())
snack=[int(input()) for _ in range(N)]

arr=[0]*N
arr[0]=snack[0]

for i in range(1,N):
    arr[i]=snack[i] #초기값 설정
    for j in range(i):  #1번째 날부터 i-1번째 날 중에서 
        if snack[j] < snack[i]: #i보다 작은 간식을 먹은 날의 누적합 비교
            arr[i]=max(arr[i],arr[j]+snack[i])  #현재 arr[i]값 보다 arr[j] 까지 먹고 i번째 날에 간식을 먹을 때 값이 더 큰 경우 갱신
print(max(arr))
