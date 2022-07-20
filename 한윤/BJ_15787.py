# 2022-07-20 (수)

from collections import deque # collections 모듈에서 deque를 가져옴

# n : 기차의 수, m : 명령의 수
n, m = map(int, input().split())

train_list = [[0] * 20 for _ in range(n)] # n개의 기차 상태 (0 : 승객이 없는 상태, 1 : 승객이 앉아있는 상태)

for _ in range(m):
    # (1) : 명령의 번호, (2) : i번째 기차, (3) : ((1)이 1, 2인 경우) x번째 좌석
    commands = list(map(int, input().split()))
    
    if commands[0] == 1: # 1번 명령어
        # commands[1] 기차에 commands[2]번째 좌석에 사람이 탑승
        train_list[commands[1] - 1][commands[2] - 1] = 1

    elif commands[0] == 2: # 2번 명령어
        # commands[1] 기차에 commands[2]번째 좌석에 사람이 하차
        train_list[commands[1] - 1][commands[2] - 1] = 0

    elif commands[0] == 3: # 3번 명령어
        temp = deque(train_list[commands[1] - 1]) # list를 deque로 변환
        # commands[1] 기차에 앉아있는 승객들이 모두 한칸씩 뒤로 이동 (20번째 자리 하차)
        temp.appendleft(0) # 왼쪽 삽입
        temp.pop() # 오른쪽 제거

        train_list[commands[1] - 1] = list(temp) # 해당 인덱스의 리스트를 교체

    else: # 4번 명령어
        temp = deque(train_list[commands[1] - 1]) # list를 deque로 변환
        # commands[1] 기차에 앉아있는 승객들이 모두 한칸씩 앞으로 이동 (1번째 자리 하차)
        temp.append(0) # 오른쪽 삽입
        temp.popleft() # 왼쪽 제거

        train_list[commands[1] - 1] = list(temp) # 해당 인덱스의 리스트를 교체

result = [] # 중복 제거된 리스트들이 들어갈 리스트

for l in train_list: # 중복 제거 작업
    if l not in result:
        result.append(l)

print(len(result)) # 중복 제거된 train_list의 리스트 수를 출력