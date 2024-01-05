from itertools import combinations

n = int(input())
count = 0
answer = []
for i in range(1, 11):
    for combi in combinations(range(0, 10), i):
        count += 1
        answer.append(int("".join(map(str, sorted(combi, reverse=True)))))

answer.sort()
if n >= len(answer):
    print(-1)
else:
    print(answer[n])