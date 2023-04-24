import sys
N = int(input())
poll = []
for _ in range(N):
    x, y = sys.stdin.readline().strip().split()
    poll.append([int(x), int(y)])

poll.sort()
size = 0
i = 0
max_index = 0
max_height = 0
for i in range(N):
    if poll[i][1] > max_height:
        max_height = poll[i][1]
        max_index = i


temp_height = poll[0][1]
temp_length = poll[0][0]

for i in range(1, max_index+1):
    if poll[i][1] >= temp_height:
        size += temp_height * (poll[i][0] - temp_length)
        temp_height = poll[i][1]
        temp_length = poll[i][0]


temp_height = poll[-1][1]
temp_length = poll[-1][0]

for i in range(N-2, max_index-1, -1):
    if poll[i][1] >= temp_height:
        size += temp_height * abs(temp_length - poll[i][0])
        temp_height = poll[i][1]
        temp_length = poll[i][0]

size += max_height

print(size)



