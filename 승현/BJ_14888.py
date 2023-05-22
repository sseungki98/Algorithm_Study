from itertools import permutations
N = int(input())
nums = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())

operators = []

if plus != 0:
    operators += ['+'] * plus

if minus != 0:
    operators += ['-'] * minus

if multiple != 0:
    operators += ['*'] * multiple

if divide != 0:
    operators += ['//'] * divide

operators_permutation = set(permutations(operators, len(operators)))

min_value = 1000000000
max_value = -1000000000
for item in operators_permutation:
    answer = nums[0]
    for i in range(len(item)):
        if item[i] == '+':
            answer = answer + nums[i+1]
        elif item[i] == '-':
            answer = answer - nums[i+1]
        elif item[i] == '*':
            answer = answer * nums[i+1]
        else:
            if answer < 0:
                answer = (-1) * (((-1) * answer) // nums[i+1])
            else:
                answer = answer // nums[i+1]

    if answer >= max_value:
        max_value = answer

    if answer <= min_value:
        min_value = answer


print(max_value)
print(min_value)