def get_nCk(n,k):
    de=1
    nu=1
    for i in range(k):
        de*=18-i
        nu*=(i+1)
    return de/nu

decimal=[2,3,5,7,11,13,17,19,23,29,31]  #
A=int(input())
B=int(input())
pA=A/100.0  #A가 일어날 확률
pB=B/100.0  #B가 일어날 확률
sumA=0
sumB=0

for i in decimal:   #n번 안에 k번 사건이 일어날 확률 = nCk*(pA**k)*((1-pA)**(18-k))
    if pA < 1:
        sumA+=get_nCk(18,i)*(pA**i)*((1-pA)**(18-i))
    if pB < 1:
        sumB+=get_nCk(18,i)*(pB**i)*((1-pB)**(18-i))

#1-두팀다 소수점수가 아닌 점수를 얻을 확률=두팀 중 적어도 한팀은 소수점수를 얻을 확률
print(1-((1-sumA)*(1-sumB)))  
