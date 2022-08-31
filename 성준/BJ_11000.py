import heapq
from sys import stdin
input=stdin.readline

N=int(input())
timeline=sorted([list(map(int,input().split())) for _ in range(N)])
room=[]

heapq.heappush(room,timeline[0][1]) #가장 먼저 시작하는 강의의 끝나는 시간 삽입

for i in range(1,N):
    if room[0] <= timeline[i][0]:   #현재 가장 빨리 끝나는 강의보다 늦게 시작하는 경우 강의실을 이어 받고
        heapq.heappop(room)
    heapq.heappush(room,timeline[i][1])     #그렇지 않은 경우는 새로운 강의실을 하나 열기만 한다.
print(len(room))                    #열려있는 강의실의 갯수 출력
