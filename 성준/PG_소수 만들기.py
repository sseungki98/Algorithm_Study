def solution(nums):
    def is_prime(number):
        for i in range(2,int(number**0.5)+1): #number의 제곱근 중 나누어지는 수가 존재한다면 소수가 아니다.
            if number%i==0:
                return False
        return True
    
    answer=0    
    for numbers in combinations(nums,3):
        if is_prime(sum(numbers)): answer+=1  #소수이면 answer+=1

    return answer
