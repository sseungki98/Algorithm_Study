from itertools import combinations

def solution(orders, course):
    answer = []
    dish = {}
    for order in orders:
        for i in course:
            for cob in combinations(list(order),i): #course의 갯수만큼 조합
                name="".join(map(str,sorted(cob)))  #오름차순으로 정렬한 name
                if name in dish: dish[name]+=1
                else: dish[name]=1
                
    max_val=2
    for key,val in sorted(dish.items(),key=lambda x:(len(x[0]),x[1]),reverse=True): #글자순으로 정렬 후(문자의 길이가 길수록 val이 작음), max_val과 비교해 출력
        if max_val<=val:        #각 길이별로 최대값과 같은 길이만 출력
            answer.append(key)
            max_val=val
            
    return sorted(answer)
