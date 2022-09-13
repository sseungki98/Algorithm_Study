import math

def solution(fees, records):
    answer = []
    car = {}
    for record in records:
        time,number,flag=record.split()
        H,M=map(int,time.split(':'))
        if number not in car: car[number]=[60*H+M,flag,0]
        else:
            if flag=='IN':            #입차라면, 입차한 시간 입력
                car[number][0]=60*H+M
                car[number][1]='IN'
            else:                     #출차라면, 요금 계산을 위한 시간 입력
                car[number][2]+=60*H+M-car[number][0]
                car[number][1]='OUT'
    for number in sorted(car.keys()): #차량 번호순으로 정렬
        if car[number][1]=='IN': car[number][2]+=1439-car[number][0]  #아직 출차기록이 없다면 23:59분 출차로 기록
        if car[number][2]<=fees[0]: answer.append(fees[1])            #기본요금 이하라면 기본요금 출력
        else: answer.append(math.ceil((car[number][2]-fees[0])/fees[2])*fees[3]+fees[1])    #올림하여 추가 요금 계산
    return answer
