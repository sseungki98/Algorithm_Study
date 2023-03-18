N = int(input())

schedule = []
for _ in range(N):
    temp = list(map(int, input().split()))
    schedule.append([temp[0], temp[1]])

money = []
for i in range(N):
    temp_money = 0
    j = i
    while True:
        if j > N-1:
            break
        temp_money = schedule[j][1]
        j += schedule[j][0]
    money.append(temp_money)
print(schedule)
print(money)