from collections import deque

N = int(input())
numbers = deque(enumerate(map(int, input().split())))
answer = []
while numbers:
    idx, number = numbers.popleft()
    answer.append(idx+1)

    if number > 0:
        numbers.rotate(-(number - 1))
    else:
        numbers.rotate(-number)

for item in answer:
    print(item, end=" ")


