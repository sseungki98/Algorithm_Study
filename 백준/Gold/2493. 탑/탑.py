N = int(input())
tops = list(map(int, input().split()))
stack = [(0, tops[0])]
answer = []

for i in range(0, N):
    flag = False
    while stack:
        if stack[-1][1] > tops[i]:
            answer.append(stack[-1][0]+1)
            stack.append((i, tops[i]))
            flag = True
            break
        else:
            stack.pop()

    if not flag:
        answer.append(0)
        stack.append((i, tops[i]))

print(*answer)





