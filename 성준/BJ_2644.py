n=int(input())
a,b=map(int,input().split())
m=int(input())
dic={ i:[] for i in range(1,n+1)}
answer=(n+1)
visited=[0]*(n+1)

def find(arr,cnt):
    global answer
    if b in arr:    #촌수를 찾았다면 최소 촌수 비교
        answer = min(answer,cnt)
    else:
        for ar in arr:
            if not visited[ar]: #방문하지 않은 경우만 탐색
                visited[ar]=1   #방문 처리
                find(dic[ar],cnt+1)
                visited[ar]=0   #방문 해제
        
for _ in range(m):  #연관된 1촌 관계를 모두 저장
    par,chi=map(int,input().split())    
    dic[chi].append(par)
    dic[par].append(chi)

find(dic[a],1)

if answer == (n+1): #촌수를 찾지 못하였다면 -1 출력
    print(-1)
else:
    print(answer)
