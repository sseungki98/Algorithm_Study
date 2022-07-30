# 2022-07-30 (토)

def solution(lottos, win_nums):
    answer = []
    
    equal_count = 0 # lottos의 번호와 win_nums의 번호가 일치하는 개수
    zero_count = 0 # lottos에서 0의 개수
    
    for x in lottos:
        if x in win_nums: # win_nums에 x가 존재하는 경우
            equal_count += 1
        if x == 0: # x의 값이 0인 경우
            zero_count += 1
    
    max_rank = equal_count + zero_count # 최고 순위의 경우는 알아볼 수 없는 번호가 당첨번호인 경우
    min_rank = equal_count # 최저 순위의 경우는 일치하는 수의 경우만 해당하는 경우
    
    # 순위 부여
    if max_rank == 6:
        max_rank = 1
    elif max_rank == 5:
        max_rank = 2
    elif max_rank == 4:
        max_rank = 3
    elif max_rank == 3:
        max_rank = 4
    elif max_rank == 2:
        max_rank = 5
    else:
        max_rank = 6
    
    if min_rank == 6:
        min_rank = 1
    elif min_rank == 5:
        min_rank = 2
    elif min_rank == 4:
        min_rank = 3
    elif min_rank == 3:
        min_rank = 4
    elif min_rank == 2:
        min_rank = 5
    else:
        min_rank = 6
    
    answer.append(max_rank)
    answer.append(min_rank)
    
    return answer