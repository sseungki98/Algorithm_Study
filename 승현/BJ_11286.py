import heapq
import sys
max_num = sys.maxsize
min_num = -sys.maxsize
N = int(input())
plushq = []
minushq = []
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap,(abs(num),num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    # if num > 0:
    #     heapq.heappush(plushq, num)
    #     continue
    # elif num < 0:
    #     heapq.heappush(minushq, -num)
    #     continue
    #
    # if plushq:
    #     plus_max = plushq[0]
    # else:
    #     plus_max = min_num
    # if minushq:
    #     minus_max = minushq[0]
    # else:
    #     minus_max = max_num
    #
    # if num == 0:
    #     if minus_max == plus_max:
    #         print(-minus_max)
    #         heapq.heappop(minushq)
    #     elif plus_max == min_num and minus_max == max_num:
    #         print(0)
    #     elif minus_max < plus_max:
    #         print(-minus_max)
    #         heapq.heappop(minushq)
    #     elif minus_max > plus_max:
    #         print(plus_max)
    #         heapq.heappop(plushq)












