T = int(input())
for _ in range(T):
    days = int(input())
    price = list(map(int, input().split()))
    price_max = price[-1]
    get_sum = 0
    for i in range(days-2, -1, -1):
        if price[i] > price_max:
            price_max = price[i]
            continue
        else:
            get_sum += price_max-price[i]

    print(get_sum)




