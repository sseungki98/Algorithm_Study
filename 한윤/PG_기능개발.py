# 2022-07-23 (토)

def solution(progresses, speeds):
    answer = []
    days_progresses = [0] * len(progresses) # 작업이 끝나기까지 남은 일수를 담는 리스트
    days_count = 0 # 현재 시점(날짜)
    
    while True: # 프로그램 작업 일수 확인
        for i in range(len(progresses)):
            if progresses[i] >= 100: # 작업이 완료된 경우엔 해당 시점을 기록하고 수행하지 않는다.
                if days_progresses[i] == 0:
                    days_progresses[i] = days_count
                continue
            progresses[i] += speeds[i]
        
        if days_progresses.count(0) == 0: # 모든 작업이 끝난 경우 반복문 탈출
            break
        days_count += 1
    
    progresses_count = 1 # 해당 일에 기능이 배포되는 개수
    progresses_value = days_progresses[0] # 해당 일의 작업 수행 일수
    
    for i in range(1, len(days_progresses)):
        if progresses_value >= days_progresses[i]: # 먼저 배포되어야 하는 작업보다 뒤의 작업의 일수가 작은 경우
            progresses_count += 1
        else: # 먼저 배포되어야 하는 작업보다 뒤의 작업의 일수가 큰 경우
            answer.append(progresses_count)
            progresses_count = 1 # 개수 초기화
            progresses_value = days_progresses[i] # 일수 초기화
    
    answer.append(progresses_count) # 나머지 작업 수행
    
    return answer