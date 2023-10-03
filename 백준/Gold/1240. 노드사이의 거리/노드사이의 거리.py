from collections import defaultdict
N, M = map(int, input().split())
treedict = defaultdict(list)


def dfs(start_idx: int, end_node: int, dist_sum: int, node_lth: int):
    dist_sum += node_lth
    if start_idx == end_node:
        print(dist_sum)
    else:
        if len(treedict[start_idx]) == 1:
            if treedict[start_idx][0][0] != end_node:
                return
        else:
            for itm in treedict[start_idx]:
                if not visited[itm[0]]:
                    visited[itm[0]] = True
                    dfs(itm[0], end_node, dist_sum, itm[1])


for _ in range(N-1):
    start, end, length = map(int, input().split())
    treedict[start].append((end, length))
    treedict[end].append((start, length))


for _ in range(M):
    node_1, node_2 = map(int, input().split())
    for item in treedict[node_1]:
        visited = [False] * (N + 1)
        visited[node_1] = True
        visited[item[0]] = True
        dist = 0
        dfs(item[0], node_2, dist, item[1])










