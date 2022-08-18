from sys import stdin
input=stdin.readline

N,K=map(int,input().split())
distance=list(map(int,input().split()))

answer=0
distance.sort()
convertIdx=0

for i in range(1,N):    #음수 양수가 변하는 index 찾기
    if distance[i] > 0 and distance[i-1] < 0:
        convertIdx=i
        break
    
if distance[convertIdx]<0:  #전부 음수일 경우 변하는 index는 N으로 처리
    convertIdx=N

for i in range(0,convertIdx,K): #K개의 책을 들고 음수 범위의 값들의 책 옮기기
    answer+=2*abs(distance[i])    

for i in range(N-1,convertIdx-1,-K): #K개의 책을 들고 양수 범위의 값들의 책 옮기기
    answer+=2*abs(distance[i])

if abs(distance[0]) < abs(distance[-1]):    #양의 정수의 절댓값이 더 큰 경우
    answer-=abs(distance[-1])
else:                                       #음의 정수의 절댓값이 더 큰 경우
    answer-=abs(distance[0])
    
print(answer)
