import sys
import heapq

input=sys.stdin.readline

for i in range(int(input())):
    K=int(input())
    page=[]
    answer=0
    for p in map(int,input().split()):  #우선순위 큐에 삽입
        heapq.heappush(page,p)
    
    while len(page)>1:                  # 큐의 크기가 1이면 종료
        sm1=heapq.heappop(page)
        sm2=heapq.heappop(page)
        answer+=sm1+sm2
        heapq.heappush(page,sm1+sm2)
        
    print(answer)
