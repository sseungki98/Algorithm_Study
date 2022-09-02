def min_prime(num):         #배열 중 가장 낮은 소수 값을 찾는 함수
    for n in num:
        flag=0
        for i in range(2,n):
            if n%i==0:
                flag=1
                break
        if not flag:
            return n
    return 0
            

N,K=map(int,input().split())
num=[i for i in range(2,N+1)] #2부터 N까지의 값 입력
answer=[]

while len(answer)<K:          #K번째 값을 찾으면 반복 종료
    m_p=min_prime(num)        #num 배열 중 가장 낮은 소수 찾기
    num.remove(m_p)           #소수 제거
    for i in range(m_p,N+1,m_p):    #소수의 배수를 answer에 삽입
        if i not in answer:
            answer.append(i)
print(answer[K-1])            #K번째 값 출력
