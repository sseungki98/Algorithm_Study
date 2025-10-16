from itertools import combinations, permutations
def solution(numbers):
    def sieve(n):
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i*i, n+1, i):
                    prime[j] = False
        return prime  # 소수 여부를 저장한 리스트 반환
    s_list = sieve(9999999)
    answer_list = []
    numbers_list = list(map(str, numbers.rstrip()))

    numbers_combi = list(permutations(numbers_list, len(numbers)))
    
    for cb in numbers_combi:
        str_cb = "".join(cb)
        for start in range(len(str_cb)):
            target = int(str_cb[0:start+1])
            
            if s_list[target] == True and target not in answer_list:
                answer_list.append(target)
    return len(answer_list)