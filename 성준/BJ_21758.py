N=int(input())

honey=[0]
honey_sum=[0]
answer=0

for i in map(int,input().split()):
    honey.append(i)
    honey_sum.append(honey_sum[-1]+i)

#꿀벌을 맨앞에 고정, 벌통을 맨뒤에 고정
tmp=honey_sum[N]-honey_sum[1]
for i in range(2,N):
    answer=max(answer,tmp+honey_sum[N]-honey_sum[i]-honey[i])

#꿀벌을 맨뒤에 고정, 벌통을 맨앞에 고정
tmp=honey_sum[N-1]
for i in range(2,N):
    answer=max(answer,tmp+honey_sum[i-1]-honey[i])

#꿀벌을 양쪽 끝엥 고정
for i in range(2,N):
    answer=max(answer,honey_sum[i]-honey_sum[1]+honey_sum[N-1]-honey_sum[i-1])
print(answer)
