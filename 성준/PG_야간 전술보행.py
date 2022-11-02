def solution(distance, scope, times):
    arr=[]
    for i in range(len(scope)):   #쌍을 유지하기 위해 배열을 합친 후
        arr.append([sorted(scope[i]),times[i]])
    arr.sort(key=lambda x:x[0])   #scope 앞의 값 기준 오름차순으로 정렬
    answer = 0
    
    for t in arr:
        sp=t[0];time=t[1]
        answer=sp[0]
        width=sp[1]-sp[0]
        if 0<answer%sum(time)<=time[0]:     #구간의 출발점에 도착했을 때, 근무 병사가 근무중인 경우 해당 위치에서 바로 return
            return answer
        if sum(time)-((answer-1)%sum(time))<=width:   #구간에 도착하였을 때, 휴식 기간 이지만, 건너야 할 width 안에 병사가 깨어나는 경우
            return answer+sum(time)-((answer-1)%sum(time))  #현재 위치에서 남은 휴식기간을 더해준 후 return
            
    return distance
