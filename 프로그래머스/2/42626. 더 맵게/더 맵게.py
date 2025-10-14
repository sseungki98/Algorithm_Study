from collections import deque
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(True):
        if len(scoville) == 1:
            last_sco = heapq.heappop(scoville)
            if last_sco < K:
                return -1
            else:
                return answer
        
        s_1 = heapq.heappop(scoville) # 제일 작은 스코빌
        s_2 = heapq.heappop(scoville) # 두번째로 작은 스코빌
        
        if s_1 >= K:
            return answer
        else:
            new_sco = s_1 + s_2 * 2
            answer += 1
            heapq.heappush(scoville, new_sco)
            
    return answer