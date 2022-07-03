N,M=map(int,input().split())
bright=list(map(int,input().split()))

for i in range(M):
    a,b,c=map(int,input().split())
    if a==1:
        bright[b-1]=c
    elif a==2:
        for k in range(b,c+1):
            bright[k-1]=(bright[k-1]-1)%2   #전구의 상태는 0 or 1이므로 -1을 해주며 2로 나눈 나머지를 취한다.
    elif a==3:
        for k in range(b,c+1):
            bright[k-1]=0
    else:
        for k in range(b,c+1):
            bright[k-1]=1
print(" ".join(map(str,bright)))
