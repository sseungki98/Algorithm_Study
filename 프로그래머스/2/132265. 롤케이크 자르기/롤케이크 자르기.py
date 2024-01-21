from collections import Counter
def solution(topping):
    answer = 0
    cnt = Counter(topping)
    a_cnt = set()
    b_cnt = set()
    for item in list(cnt.keys()):
        a_cnt.add(item)
    while topping:
        top = topping.pop()
        b_cnt.add(top)
        cnt[top] -= 1
        if cnt[top] == 0:
            a_cnt.remove(top)
            
        if len(a_cnt) == len(b_cnt):
            answer += 1
    return answer