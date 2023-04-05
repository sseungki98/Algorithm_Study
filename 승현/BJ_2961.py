from itertools import combinations
N = int(input())
flavor = []

for _ in range(N):
    a, b = map(int, input().split())
    flavor.append([a,b])

minn = 99999999
for i in range(1, N+1):
    idx = list(combinations(flavor, i))
    if i == 1:
        for item in idx:
            for j in range(len(item)):
                minn = min(minn, abs(item[j][0] - item[j][1]))
    else:
        for item in idx:
            sour = 1
            bitter = 0
            for j in range(len(item)):
                sour *= item[j][0]
                bitter += item[j][1]

            minn = min(minn, abs(bitter - sour))

print(minn)

