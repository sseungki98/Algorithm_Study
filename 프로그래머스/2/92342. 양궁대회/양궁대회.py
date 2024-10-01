from itertools import product
def solution(n, info):
    answer = []
    pd = list(product([0,1], repeat= 10)) # 1이 라이언이 승리하는 경우
    max_diff = -1
    for item in pd:
        last_arrow = n
        win_flag = False
        apc = 0
        lion = 0
        temp_arrow = [0] * 11
        for i in range(len(item)):
            if item[i] == 1: # LION 이긴경우
                if last_arrow - (info[i] + 1) >= 0: # 화살이 어피치 + 1 가능한 경우
                    last_arrow -= (info[i] + 1)
                    temp_arrow[i] = info[i] + 1
                    lion += (10 - i)
                else:
                    temp_arrow[i] = 0
                    if info[i] != 0:
                        apc += (10 - i) # 화살 부족하면 어피치가 승리
            else: # 어피치가 이긴 경우
                temp_arrow[i] = 0
                if info[i] != 0: # 어피치도 0발을 맞추지 않았다면
                    apc += (10 - i)
                    
        if lion > apc:
            diff = lion - apc
            if diff > max_diff:
                answer = temp_arrow
                temp_arrow[-1] += last_arrow
                max_diff = diff

            elif diff == max_diff:
                temp_arrow[-1] += last_arrow
                if answer[-1] < temp_arrow[-1]:
                    answer = temp_arrow
                else:
                    temp_answer = answer[:]
                    t_temp_arrow = temp_arrow[:]
                    while True:
                        if not temp_answer:
                            break
                        ans_pop = temp_answer.pop()
                        arrow_pop = t_temp_arrow.pop()
                        if ans_pop == arrow_pop:
                            continue
                        elif arrow_pop > ans_pop:
                            answer = temp_arrow
                        break
                                    
            
    if answer == []:
        answer = [-1]

    return answer