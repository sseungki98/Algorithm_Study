#가장 앞의 남은 일수를 확인한 정답 풀이
import math
def solution(progresses, speeds):
    answer = []
    k=0
    while k<len(progresses):
        if progresses[k]>=100:  #이미 완성되었으면 다음반복 진행
            k+=1
            continue
        tmp=0
        time=100-progresses[k]  #남은 진행도 계산
        state=0
        remaining=math.ceil(time/speeds[k]) #남은 일수 계산
        for i in range(len(progresses)):
            progresses[i]+=remaining*speeds[i]  #현재 idx의 진행도가 100의 일자만큼 다른 progresses 진행
        
        for i in range(k,len(progresses)):
            if progresses[i] >=100: #현재 idx가 완성되는 동안 뒤의 완성도가 100이 된 갯수 탐색
                tmp+=1
            else:
                state=1 #그렇지 않다면 끊긴 곳의 idx 저장
                k=i
                break
        answer.append(tmp)  #동시에 배포 할 기능의 갯수를 answer에 추가
        if state: #idx의 마지막 위치를 저장해두었으므로 다음 반복 진행
            continue
        else: #완성된 위치의 다음 progress idx부터 다음 반복 짆애
            k+=1
    return answer
  
  #zip을 활용한 정답 풀이
  def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
