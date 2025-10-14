from collections import deque
def solution(priorities, location):
    answer = 0
    p_dq = deque(priorities)
    priorities_sort = sorted(priorities)
    for i in range(len(p_dq)):
        p_dq[i] = [p_dq[i], i]
    
    while(p_dq):
        high_p_process = priorities_sort.pop() # 가장 높은 우선순위
        while True:
            now_process = p_dq.popleft()
            if now_process[0] == high_p_process:
                answer += 1
                if now_process[1] == location:
                    return answer
                else:
                    break
            else:
                p_dq.append(now_process)      
                    
        
    return answer