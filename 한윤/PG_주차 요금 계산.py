# 2022-09-18 (일)

import math

def solution(fees, records):
    answer = []
    
    parkingNum = [] # 입차되어있는 차량의 번호를 담는 리스트
    parkingTime = [] # 입차되어있는 차량의 시각을 담는 리스트
    carNum = [] # 청구할 주차 요금이 있는 차량의 번호를 담는 리스트
    carTime = [] # 청구할 주차 요금이 있는 차량의 주차 시간을 담는 리스트
    
    carFee = [] # 각 차량번호 별 청구할 주차 요금을 담는 리스트 (결과 리스트)
    
    # (1) 메인 연산
    for i in range(len(records)):
        # 공백을 기준으로 시각, 차량번호, 내역을 리스트 원소로 분리
        records[i] = records[i].split()
        
        if records[i][2] == "IN": # 주차되어있지 않은 차량의 경우
            parkingNum.append(records[i][1])
            parkingTime.append(records[i][0])
        else: # 주차되어있는 차량의 경우
            idx = parkingNum.index(records[i][1]) # 해당 차량번호를 가지는 index
            outTime = int(records[i][0][0:2]) * 60 + int(records[i][0][3:5]) # 출차 시간 (분)
            inTime = int(parkingTime[idx][0:2]) * 60 + int(parkingTime[idx][3:5]) # 입차 시간 (분)
            
            totalTime = outTime - inTime # 주차되어있던 시간을 계산
            if records[i][1] not in carNum: # 이전에 주차 기록이 없는 차량의 경우
                carNum.append(records[i][1])
                carTime.append(totalTime)
            else: # 이전에 주차 기록이 있는 차량의 경우
                car_idx = carNum.index(records[i][1])
                carTime[car_idx] += totalTime
            
            # 차량을 출차했으므로, 이전의 입차된 기록을 삭제
            del parkingNum[idx]
            del parkingTime[idx]
    
    # (2) 나머지 연산
    if parkingNum: # 입차된 기록만 존재하고 출차 기록이 존재하지 않는 경우 처리
        for i in range(len(parkingNum)):
            outTime = 23 * 60 + 59 # 출차 시간 (23:59) (분)
            inTime = int(parkingTime[i][0:2]) * 60 + int(parkingTime[i][3:5]) # 입차 시간 (분)
            
            totalTime = outTime - inTime # 주차되어있던 시간을 계산
            if parkingNum[i] not in carNum: # 이전에 주차 기록이 없는 차량의 경우
                carNum.append(parkingNum[i])
                carTime.append(totalTime)
            else: # 이전에 주차 기록이 있는 차량의 경우
                car_idx = carNum.index(parkingNum[i])
                carTime[car_idx] += totalTime
    
    # (3) 주차 시간(분) => 주차 요금 연산
    for i in range(len(carNum)):
        if carTime[i] <= fees[0]: # 주차 시간이 기본 시간보다 작은 경우
            carFee.append([carNum[i], fees[1]]) # 기본 요금만 계산
        else: # 주차 시간이 기본 시간보다 큰 경우
            totalTime = carTime[i] - fees[0]
            carFee.append([carNum[i], fees[1] + (math.ceil(totalTime / fees[2]) * fees[3])])
            
    carFee.sort(key = lambda x : x[0]) # 차량번호를 기준으로 오름차순 정렬
    for x in carFee:
        answer.append(x[1])
    
    return answer

# 실행예시 (1)
print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# 결과 값 : [14600, 34400, 5000]

# 실행예시 (2)
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# 결과 값 : [0, 591]

# 실행예시 (3)
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
# 결과 값 : [14841]