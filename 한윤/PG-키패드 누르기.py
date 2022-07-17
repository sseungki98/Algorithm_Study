# 2022-07-17 (일)

def solution(numbers, hand):
    answer = ''

    left_loc = 10 # 왼손 엄지손가락 위치 (시작 지점으로 초기화)
    right_loc = 12 # 오른손 엄지손가락 위치 (시작 지점으로 초기화)

    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7: # 키패드 왼쪽의 숫자인 경우, 왼손 엄지손가락 사용
            answer += 'L'
            left_loc = numbers[i] # 왼손 위치 교체
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9: # 키패드 오른쪽의 숫자인 경우, 오른손 엄지손가락 사용
            answer += 'R'
            right_loc = numbers[i] # 오른손 위치 교체
        else: # 키패드 중앙의 숫자인 경우
            if numbers[i] == 0: # 0인 경우, 11으로 교체
                numbers[i] = 11

            left_value = abs(left_loc - numbers[i])
            right_value = abs(right_loc - numbers[i])

            left_dist = (left_value // 3) + (left_value % 3) # 왼손 거리 계산
            right_dist = (right_value // 3) + (right_value % 3) # 오른손 거리 계산

            if left_dist > right_dist: # 오른손 엄지손가락이 더 가까운 경우
                answer += 'R'
                right_loc = numbers[i] # 오른손 위치 교체
            elif left_dist < right_dist: # 왼손 엄지손가락이 더 가까운 경우
                answer += 'L'
                left_loc = numbers[i] # 왼손 위치 교체
            else: # 두 엄지손가락의 거리가 같은 경우
                if hand == "left": # 왼손잡이인 경우
                    answer += 'L'
                    left_loc = numbers[i]
                else: # 오른손잡이인 경우
                    answer += 'R'
                    right_loc = numbers[i]

    return answer
