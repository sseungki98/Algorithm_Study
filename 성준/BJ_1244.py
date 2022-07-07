from sys import stdin

N=int(input())
switch=list(map(int,stdin.readline().split()))
K=int(input())
for _ in range(K):
    gender,number=map(int,stdin.readline().split())
    if gender==1:   #남자인 경우
        for i in range(number,N+1,number): 
            switch[i-1]=(switch[i-1]-1)%2   #배수들 스위치 전환
    elif gender==2: #여자인 경우
        neighborIdx=1 #이웃값 탐색
        while 1<=(number-neighborIdx) and (number+neighborIdx)<=N:    #옆라인부터 값 증가
            if switch[number-neighborIdx-1]==switch[number+neighborIdx-1]:
                neighborIdx+=1
            else:   #값이 같지 않으면 종료
                break
        neighborIdx-=1    #반복문이 실행되었다면 i-1번 이웃한 값들까지 유효 & 실행되지 않았다면 자기자신만 유효
        for k in range(number-neighborIdx,number+neighborIdx+1):
            switch[k-1]=(switch[k-1]-1)%2
n=0
while N>20: #20줄씩 끊어서 출력
    print(" ".join(map(str,switch[n:n+20])))
    n+=20
    N-=20
print(" ".join(map(str,switch[n:n+N]))) #마지막줄 출력
