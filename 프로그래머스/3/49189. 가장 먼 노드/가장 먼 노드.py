from collections import defaultdict, Counter
import heapq
def solution(n, edge):
    answer = 0
    route = defaultdict(list)
    
    for vx in edge:
        v1, v2 = vx[0], vx[1]
        route[v1].append([1,v2])
        route[v2].append([1,v1])
    
    INF = float('inf')
    distance = [INF] * (n+1)
    dq = []
    
    def djs(start_node):
        distance[start_node] = 0
        hq = []
        heapq.heappush(hq, (0, start_node))
        while hq:
            dist, node = heapq.heappop(hq)
            if distance[node] < dist:
                continue
            
            for next in route[node]:
                cost = distance[node] + next[0]
                if distance[next[1]] > cost:
                    distance[next[1]] = cost
                    heapq.heappush(hq, (cost, next[1]))
    djs(1)

    max_dist = max(d for d in distance if d != INF)

    answer = distance.count(max_dist)
            

    return answer