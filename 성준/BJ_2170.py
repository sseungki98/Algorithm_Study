import sys
input=sys.stdin.readline

N=int(input())
number=[list(map(int,input().split())) for _ in range(N)]
number.sort()
left=number[0][0]
right=number[0][1]
answer=0

for t in range(1,N):  
    if number[t][0]<=right:           #현재 출발점이 이 전의 도착점 이전인 경우 연결되어 있으므로 도착점만 최대값으로 변경
        right=max(right,number[t][1])
    else:                             #현재 출발점이 이전 도착점보다 튀어나왔을 경우, 새로 연결된 선이므로 값을 이 전 선분의 값을 더해주고 시작점, 도착점 변경
        answer+=(right-left)
        left,right=number[t][0],number[t][1]
    
answer+=right-left                    #마지막 선분의 값 추가

print(answer)
