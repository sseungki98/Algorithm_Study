import sys
N, M = map(int, input().split())
keywords = {}

res = N

for _ in range(N):
    line = sys.stdin.readline().rstrip()
    keywords[line] = 1

for _ in range(M):
    write_keyword = sys.stdin.readline().rstrip().split(',')
    for item in write_keyword:
        if item in keywords.keys():
            if keywords[item] == 1:
                keywords[item] -= 1
                res -= 1

    print(res)

