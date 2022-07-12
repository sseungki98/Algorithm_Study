N,T=map(int,input().split())
answer=1000000

for _ in range(N):
    S,I,C=map(int,input().split())  #시작시간, 간격, 대수
    if S >= T:  #버스가 아직 운행을 시작하지 않은 경우
        if answer == -1:
            answer=S-T
        else:
            answer=min(answer,S-T) 
    else:   #버스가 이전부터 운행을 시작한 경우
        if S+((C-1)*I) < T: #마지막 버스의 출발시간이 영식의 도착시간보다 빠른 경우
            if answer == 1000000:
                answer=-1
        else:
            while True: #무조건 break문에 도달하므로 버스가 도착 시간에 도달할 때 까지 반복
                S+=I    #다음 버스 도착시간
                if S >= T:  #버스가 도착시간 이후 도착한 경우
                    if answer == -1:    #이전에 -1을 경우 예외처리
                        answer=S-T
                    else:
                        answer=min(answer,S-T)
                        break
print(answer)
