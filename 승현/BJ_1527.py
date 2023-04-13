def goldminsoo(number):
    global result
    if a <= number <= b:
        result += 1
    elif number > b:
        return

    goldminsoo(number * 10 + 4)
    goldminsoo(number * 10 + 7)


a, b = map(int, input().split())
result = 0

goldminsoo(4)
goldminsoo(7)

print(result)


