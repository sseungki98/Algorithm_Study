import math

N=int(input())
flag=False

def check_p(k):   #팰린드롬의 여부 판별
    if k==k[::-1]:
        return True
    return False

def check_isprime(k): #소수 여부 판별
    if k==1:
        return False
    for i in range(2,int(math.sqrt(k))+1):  # ex) 15의 약수는 1,3,5,15 인데 이 때 15의 제곱수인 3.xx의 3까지 확인했을 때 약수가 없다면 이는 소수임을 응용한 문제
        if k%i==0:
            return False
    return True

while not flag:
    flag=check_p(str(N)) and check_isprime(N)
    N+=1
print(N-1)
