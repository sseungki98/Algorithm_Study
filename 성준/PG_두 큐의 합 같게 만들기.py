from collections import deque

def solution(queue1, queue2):

    dq1=deque(queue1)
    dq2=deque(queue2)
    sum_q1=sum(queue1)  #sum 연산은 n만큼의 시간이 소요됨으로 sum값을 먼저 구한 후 값을 +,-해서 유지시켜준다.
    sum_q2=sum(queue2)
    
    for i in range(len(queue1)*3):  #한쪽에 극단 적으로 쏠린 경우를 대비해 *3만큼의 반복을 해준다.
        if sum_q1==sum_q2:  #합이 같으면 종료
            return i
        if sum_q1 > sum_q2: #합이 더 큰쪽의 앞의 값을 빼본다.
            sum_q1-=dq1[0]
            sum_q2+=dq1[0]
            dq2.append(dq1.popleft())
        else:
            sum_q1+=dq2[0]
            sum_q2-=dq2[0]
            dq1.append(dq2.popleft())
    return -1 #len(queue1)*3만큼의 반복을 했는데도 값이 같아지지 않으면 같은 경우의 수가 없다고 판단하고 -1을 return 한다.
