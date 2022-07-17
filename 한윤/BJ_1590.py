# 2022-07-13 (수)

# n : 버스의 개수, t : 영식이가 버스터미널에 도착하는 시간
n, t = map(int, input().split())
data = []
for _ in range(n): # 입력
    # s : 각 버스의 시작 시간, i : 간격, c : 대수
    s, i, c = map(int, input().split())
    data.append([s, i, c])

min_time = 10000000 # 영식이가 기다려야 하는 최소 시간
for i in range(n): # 각 버스마다 확인 => 최소 시간 갱신
    for j in range(data[i][2]):
        if (data[i][0] + (data[i][1] * j) - t) >= 0 and (data[i][0] + (data[i][1] * j) - t) < min_time:
            min_time = data[i][0] + (data[i][1] * j) - t

if min_time == 10000000: # 최소 시간이 갱신되지 않은 경우
    print(-1)
else:
    print(min_time)