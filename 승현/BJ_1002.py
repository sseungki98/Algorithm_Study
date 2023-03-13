import math
t_num = int(input())
for _ in range(t_num):
    data = list(map(int, input().split()))  # x1, y1, r1, x2, y2, r2
    (x1, y1) = data[0], data[1]
    (x2, y2) = data[3], data[4]
    (r1, r2) = data[2], data[5]
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if dist == 0 and r1 == r2:
        print(-1)
    elif abs(r2-r1) < dist < r1+r2:
        print(2)
    elif dist == r1+r2 or dist == abs(r2-r1):
        print(1)
    else:
        print(0)
