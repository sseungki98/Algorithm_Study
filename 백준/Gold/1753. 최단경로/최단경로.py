from collections import defaultdict
import heapq
import sys
V, E = map(int, input().split())
start = int(input())
store = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    store[u].append([w, v])
INF = float('inf')
distance = [INF] * (V+1)
hq = []
distance[start] = 0
heapq.heappush(hq, [0, start])
while hq:
    dist, point = heapq.heappop(hq)
    if distance[point] > dist:
        continue
    for next in store[point]:
        new_distance = distance[point] + next[0]
        if distance[next[1]] > new_distance:
            distance[next[1]] = new_distance
            heapq.heappush(hq, [new_distance, next[1]])

for i in range(V):
    out = distance[i+1]
    if out == INF:
        print('INF')
    else:
        print(out)