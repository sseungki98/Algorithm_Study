N,M=map(int,input().split())
graph=[list(map(int,input())) for _ in range(N)]
answer=-1

for i in range(N):
    for j in range(M):
        for a in range(-N,N):         #행의 등차
            for b in range(-M,M):     #열의 등차
                num=''
                x,y=i,j
                while 0<=x<N and 0<=y<M:
                    num+=str(graph[x][y])
                    if a==0 and b==0: #등차가 0이면 무한루프에 빠지게 된다.
                        break
                    if int(int(num)**(0.5))**2==int(num): #제곱수 판별
                        answer=max(answer,int(num))
                    x+=a              #행의 등차만큼 증가
                    y+=b              #열의 등차만큼 증가
print(answer)
