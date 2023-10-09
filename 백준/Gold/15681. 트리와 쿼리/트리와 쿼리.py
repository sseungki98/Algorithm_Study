from collections import defaultdict
import sys
sys.setrecursionlimit(100000000)
N, R, Q = map(int, input().split())
store = defaultdict(list)
tree = defaultdict(set)
size = {}
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    store[a].append(b)
    store[b].append(a)



def makeTree(current_node: int, parent: int):
    for item in store[current_node]:
        if item != parent:
            tree[current_node].add(item)
            makeTree(item, current_node)


makeTree(R, R)
def countSubtreeNodes(current_node: int):
    size[current_node] = 1
    for item in tree[current_node]:
        countSubtreeNodes(item)
        size[current_node] += size[item]

countSubtreeNodes(R)
for _ in range(Q):
    U = int(sys.stdin.readline())
    print(size[U])
