import sys
stack_2 = []

stack_1 = list(sys.stdin.readline())
stack_1.pop()

N = int(sys.stdin.readline())
for _ in range(N):
    command = sys.stdin.readline()
    if command[0] == 'L':
        if len(stack_1) != 0:
            stack_2.append(stack_1.pop())
    elif command[0] == 'D':
        if len(stack_2) != 0:
            stack_1.append(stack_2.pop())
    elif command[0] == 'B':
        if len(stack_1) != 0:
            stack_1.pop()
    elif command[0] == 'P':
        stack_1.append(command[2])
stack_2.reverse()
print(''.join(stack_1 + stack_2))

