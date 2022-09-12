def solution(n, k):
    def convert(n,k):   #진수 변환
        result=''
        while n>0:
            result+=str(n%k)
            n//=k
        return result[::-1]
    
    def is_prime(i):    #소수 판별
        if int(i)<=1: return False
        for k in range(2,int(int(i)**(0.5))+1):
            if int(i)%k==0: return False
        return True
    
    answer=0
    for i in convert(n,k).split('0'):   #0을 기준으로 split
        if i:   #i가 존재한다면
            if is_prime(i): answer+=1   #소수라면 +1
    return answer
