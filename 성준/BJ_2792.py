from sys import stdin
import math

N,M=map(int,stdin.readline().split())
jewls=[int(stdin.readline()) for _ in range(M)]

left=1
right=max(jewls)

while left <= right:
    total=0
    mid=(left+right)//2 #한사람이 가져 가게 될 보석 수
        
    for jewl in jewls:  #각 보석을 mid만큼 가져 갈 수 있는 사람의 수를 total에 더한다.
        total+=math.ceil(jewl/mid)
        
    if total > N:   #보석을 가져간 사람이 주어진 N보다 크면 각자 더 많은 보석을 가져가야 한다.
        left=mid+1
    else:   #질투심을 줄이기 위해 한 사람이 가져가는 보석의 수를 줄이는 경우
        right=mid-1
print(left)
