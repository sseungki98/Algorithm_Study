import sys
from itertools import combinations
input=sys.stdin.readline

N,M=map(int,input().split())
town=[[float('inf')]*N for i in range(N)]
answer=[0,0,float('inf')]

for k in range(M):
    a,b=map(int,input().split())
    town[a-1][b-1]=1
    town[b-1][a-1]=1

for i in range(N):        #플로이드-워셜 알고리즘을 통한 각 노드별 최소거리
    town[i][i]=0
    for j in range(N):
        for k in range(N):
            town[j][k]=min(town[j][k],town[j][i]+town[i][k])
            
for a,b in combinations([i+1 for i in range(N)],2):   #2개의 치킨집 선택
    tmp=0
    for i in range(N):                                #노드에서 가장 적은 치킨집의 거리
        tmp+=min(town[a-1][i],town[b-1][i])*2       
    if tmp<answer[2]:                                 #최소의 노드부터 선택하므로, 최소값 갱신때만 answer 변경
        answer[0],answer[1],answer[2]=a,b,tmp
print(*answer)  
