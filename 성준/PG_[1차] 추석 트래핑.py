def solution(lines):
    answer = 0
    historys = []
    for line in lines:
        day,time,running=line.split()       #날짜, 시간, 처리시간으로 나눠준다.
        H,M,S=map(float,time.split(':'))    #시간을 시:분:초로 나누어준다.
        end_time=int((H*3600+M*60+S)*1000)  #시,분,초를 합산해 int형 수로 표현하여 준다.
        running_time=int(float(running.split('s')[0])*1000)   #처리시간 또한 int형으로 변환하여 준다.
        start_time=end_time-running_time+1    #시작 시간은 끝나는시간-처리시간+1 이다.
        historys.append([start_time,end_time])
        
    for i in range(len(historys)):    #끝나는 시간 순으로 정렬되어 있으므로
        cnt=1
        end=historys[i][1]
        for k in range(i+1,len(historys)):  #j번째의 시작시간이 i번째의 끝나는 시간 이전이라면 동시에 처리된다
            if end > historys[k][0]-1000:
                cnt+=1
        answer=max(answer,cnt)
    return answer
