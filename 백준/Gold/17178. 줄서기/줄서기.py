from collections import deque

N = int(input())
store = deque()
wait_stack = []
entrance_stack = []
for _ in range(N):
    temp_list = list(map(str, input().split()))
    for item in temp_list:
        alpha, number = item.split('-')
        store.append((alpha, int(number)))

sorted_dq = deque(sorted(store, key=lambda x: (x[0], x[1])))
min_alpha, min_number = sorted_dq.popleft()


def solution():
    global min_alpha, min_number
    while store:
        _alpha, _number = store.popleft()
        if _alpha == min_alpha and _number == min_number:
            entrance_stack.append((_alpha, _number))
            if sorted_dq:
                min_alpha, min_number = sorted_dq.popleft()
                continue
        elif wait_stack and (wait_stack[-1][0] == min_alpha and wait_stack[-1][1] == min_number):
            while wait_stack and (wait_stack[-1][0] == min_alpha and wait_stack[-1][1] == min_number):
                entrance_stack.append(wait_stack.pop())
                if sorted_dq:
                    min_alpha, min_number = sorted_dq.popleft()
        wait_stack.append((_alpha, _number))

    if wait_stack:
        while wait_stack:
            wait_alpha, wait_number = wait_stack.pop()
            if wait_alpha == min_alpha and wait_number == min_number:
                entrance_stack.append((wait_alpha, wait_number))
                if len(sorted_dq) == 0:
                    return 'GOOD'
                min_alpha, min_number = sorted_dq.popleft()
            else:
                return 'BAD'
    else:
        return 'GOOD'


print(solution())
