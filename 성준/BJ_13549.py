from sys import stdin
from collections import deque

N,K=map(int,stdin.readline().split())
g_list=[0]*100001
visited=[0]*100001

def bfs():
    dq=deque()
    dq.append(N)
    
    while dq:
        x=dq.popleft()
        if x==K:              #목적지에 도달하면 결과 출력후 함수 종료
            print(g_list[x])
            return
        if 0<=2*x<=100000 and not visited[2*x]:   #순간이동시에는 소모값이 0초이므로, 1/2의 위치까지 걸리는 시간 그대로를 가져온다.
            g_list[2*x]=g_list[x]
            dq.append(2*x)
            visited[2*x]=1
        for k in (x-1,x+1):                       #정상이동시에는 소모값이 1초이므로, x-1 or x+1까지의 위치에서 걸리는 시간의 +1을 해준다.
            if 0<=k<=100000 and not visited[k]:
                g_list[k]=g_list[x]+1
                dq.append(k)
                visited[k]=1
bfs()
