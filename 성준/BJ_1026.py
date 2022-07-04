N=int(input())
A_list=list(map(int,input().split()))
B_list=list(map(int,input().split()))

A_list.sort() #오른차순으로 정렬
B_list.sort(reverse=True) #내림차순으로 정렬
answer=0

for i in range(N):  #최솟값을 얻기 위해서는, 큰 값을 작은값들과 곱해졌을 때 최소의 결과를 얻을 수 있으므로
    answer+=A_list[i]*B_list[i]   #가장 큰 값은 가장 작은 값과, 그 다음 큰 값은 그 다음 작은 값과 매칭시켜준다.
    
print(answer)
