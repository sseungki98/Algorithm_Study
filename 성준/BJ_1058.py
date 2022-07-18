from sys import stdin

def findFriend(start,end):
    global cnt
    global visited
    for k in range(N):
        if friend[end][k]=='Y' and not visited[k]:  #친구의 친구 탐색
            visited[k]=1
            cnt[start]+=1

N=int(input())
friend=[]
cnt=[0]*N

for i in range(N):
    friend.append(list(map(str,stdin.readline().strip())))

for i in range(N):
    visited=[0]*N
    visited[i]=1
    for j in range(N):
        if friend[i][j]=='Y':
            if not visited[j]:  #방문된 곳이 아니라면 cnt 증가 후 해당 idx의 친구 탐색
                visited[j]=1
                cnt[i]+=1
                findFriend(i,j)
            else:   #방문된 곳이라면, 해당 idx를 방문해서 친구만 탐색
                findFriend(i,j)
print(max(cnt))
