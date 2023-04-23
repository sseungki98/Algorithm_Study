N = int(input())
budget = list(map(int, input().split()))
max_budget = int(input())
budget.sort()
size = len(budget)
if sum(budget) <= max_budget:
    print(max(budget))
else:
    temp_sum = 0
    for i in range(len(budget)):
        if (temp_sum + budget[i] * (size - i)) <= max_budget:
            temp_sum += budget[i]
        else:
            print((max_budget - temp_sum) // (size - i))
            break

