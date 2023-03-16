number = list(map(int, input().split()))

N = number[0]
BN = number[1]

point = {}
count = 0
end_flag = False
init_point = 0
for i in range(N):
    p_num = int(input())
    point[i] = p_num

for _ in range(N):
    if point[init_point] == BN:
        count += 1
        end_flag = True
        break
    else:
        init_point = point[init_point]
        count += 1

if end_flag == False:
    print(-1)
else:
    print(count)