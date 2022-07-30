def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)  #0의 갯수 count
    cnt = 0
    
    for lotto in lottos:  #일치하는 숫자 탐색
        if lotto in win_nums:
            cnt+=1
    
    return min(7-(cnt+zero_cnt),6),min(7-cnt,6) #7이 나올 수 있는 경우 예외처리 및 zero를 사용한 순위와 사용하지 않은 순위 반환
