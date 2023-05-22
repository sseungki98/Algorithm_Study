from sys import stdin
import heapq
population, centi_height, hammer_count = map(int, input().split())
hm_count = 0
heights = []
for _ in range(population):
    value = int(stdin.readline().strip())
    heapq.heappush(heights, (-value, value))


for _ in range(hammer_count):
    if heights[0][1] < centi_height:
        break
    else:
        max_value = heapq.heappop(heights)[1]
        if max_value == 1:
            hm_count += 1
            heapq.heappush(heights, (-1,1))
            break
        hm_count += 1
        heapq.heappush(heights, (-(max_value // 2), max_value // 2))


max_value = heapq.heappop(heights)[1]
if hm_count == hammer_count:
    if max_value < centi_height:
        print('YES')
        print(hm_count)
    else:
        print('NO')
        print(max_value)
elif hm_count < hammer_count:
    if centi_height <= max_value:
        print('NO')
        print(max_value)
    else:
        print('YES')
        print(hm_count)
