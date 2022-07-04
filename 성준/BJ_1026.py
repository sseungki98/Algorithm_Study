N=int(input())
A_list=list(map(int,input().split()))
B_list=list(map(int,input().split()))
answer=0

for i in range(N):
    answer+=A_list.pop(A_list.index(min(A_list)))*B_list.pop(B_list.index(max(B_list))) #A의 최소값과 B의 최대값을 빼와주며 곱해준다.
print(answer)
