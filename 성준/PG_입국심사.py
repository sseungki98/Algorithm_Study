def solution(n, times):
    answer = 0
    left=min(times)     #최소시간에 한명의 입국심사만 할 경우 최소
    right=max(times)*n  #모든 사람이 가장 늦게 걸리는 입국 심사로 갈 경우 최악
    while left <= right:
        checked=0   #입국심사 완료자
        mid=(left+right)//2
        
        for time in times:      #해당 시간내에 입국심사를 몇명 통과시킬 수 있는지 탐색
            checked+=mid//time
            
        if checked>=n:  #입국심사 통과자가 n보다 같거나 많으면
            answer=mid  #중간값을 answer에 저장 후
            right=mid-1 #더 적은 시간대로 탐색 가능한지 탐색한다
        else:           #해당시간 내에 입국심사를 전부 완료하지 못하였다면
            left=mid+1  #left값을 증가 시킨다
    return answer
