from sys import stdin
input=stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    stack=[]
    for _ in range(N):
        a,b=map(int,input().split())
        stack.append([a,b])
    stack.sort()  #앞의 성적순으로 먼저 정렬
    min_val=stack[0][1]
    for a,b in stack:
        if b > min_val: #앞에 나보다 더 높은 순위를 가진 사람이 있다면, 둘 다 나보다 높은 것이므로 탈락
            N-=1
        else:
            min_val=b
    print(N)
