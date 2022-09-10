import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def dfs(idx,cnt):
    global answer
    if cnt==4:    #깊이가 4이면 A-B-C-D-E를 만족하는 관계 탄생
        answer=1
        return
    for i in friend[idx]: #시간 단축을 위해 연결되어 있는 요소만 탐색
        if not visited[i]:
            visited[i]=1
            dfs(i,cnt+1)
            visited[i]=0

N,M=map(int,input().split())
friend=[[] for _ in range(N)] 
visited=[0]*N
answer=0

for i in range(M):
    a,b=map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(N):
    visited[i]=1
    dfs(i,0)
    if answer: break  #answer이 1이 되었다면 반복 종료
    visited[i]=0
print(answer)
