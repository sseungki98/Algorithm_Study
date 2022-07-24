# 2022-07-24 (일)

n = int(input()) # n : 스위치 개수
switch = list(map(int, input().split())) # 스위치의 상태

m = int(input()) # m : 학생 수
for _ in range(m):
    # stu_gender : 학생의 성별, stu_num : 학생이 받은 수
    stu_gender, stu_num = map(int, input().split())
    
    if stu_gender == 1: # 남학생인 경우
        i = 1
        temp = stu_num * i # stu_num의 배수
        while temp <= n:
            if switch[temp - 1] == 0: # 상태 변경
                switch[temp - 1] = 1
            else:
                switch[temp - 1] = 0
            
            i += 1
            temp = stu_num * i # 배수로 만듦
    
    else: # 여학생인 경우
        i = stu_num - 1 # 왼쪽
        j = stu_num + 1 # 오른쪽
        while i > 0 and j <= n:
            if switch[i - 1] == switch[j - 1]: # 상태가 같은 경우
                if switch[i - 1] == 0:
                    switch[i - 1] = 1
                    switch[j - 1] = 1
                else:
                    switch[i - 1] = 0
                    switch[j - 1] = 0
                i -= 1
                j += 1
            else: # 상태가 다른 경우
                break

        if switch[stu_num - 1] == 0: # 자기 자신의 상태 변경
            switch[stu_num - 1] = 1
        else:
            switch[stu_num - 1] = 0

x_count = 0
for x in switch: # 출력
    print(x, end = ' ')
    x_count += 1
    if x_count % 20 == 0: # 줄바꿈
        print()

# 문제에 따른 출력형식에 대한 주의 필요