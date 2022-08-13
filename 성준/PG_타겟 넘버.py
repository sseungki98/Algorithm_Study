from itertools import permutations
answer = 0

def solution(numbers, target):
    def dfs(cnt,ans):
        global answer
        if cnt >= len(numbers): #cnt가 numbers의 길이를 넘어가면 반복 종료
            if ans==target:
                answer+=1
            return 
        dfs(cnt+1,ans+numbers[cnt])
        dfs(cnt+1,ans-numbers[cnt])
        
    dfs(0,0)
    return answer
