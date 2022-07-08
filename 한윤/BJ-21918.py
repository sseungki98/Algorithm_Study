# 2022-07-05 (화)

# n : 전구의 개수, m : 명령어의 개수
n, m = map(int, input().split())

# n개의 전구가 현재 어떤 상태 s인지 (0 : 꺼져있는 상태, 1 : 켜져있는 상태)
data = list(map(int, input().split()))

command_1 = [] # a번째 명령어
command_2 = [] # i or l
command_3 = [] # x or r

for _ in range(m):
    a, b, c = map(int, input().split())

    command_1.append(a)
    command_2.append(b)
    command_3.append(c)

for i in range(m):
    if command_1[i] == 1: # 1번째 명령어인 경우
        data[command_2[i] - 1] = command_3[i]
    
    elif command_1[i] == 2: # 2번째 명령어인 경우
        for j in range(command_2[i] - 1, command_3[i]):
            if data[j] == 0: # 꺼져있는 전구를 킨다.
                data[j] = 1
            else: # 켜져있는 전구를 끈다.
                data[j] = 0
    
    elif command_1[i] == 3: # 3번째 명령어인 경우
        for j in range(command_2[i] - 1, command_3[i]):
            data[j] = 0 # 전구를 끈다.
    
    else: # 4번째 명령어인 경우
        for j in range(command_2[i] - 1, command_3[i]):
            data[j] = 1 # 전구를 킨다.

for x in data:
    print(x, end=' ')