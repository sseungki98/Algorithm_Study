topping_num = int(input())
price = list(map(int, input().split()))
dough_price = price[0]
topping_price = price[1]
dough_cal = int(input())
topping_cal = []
cal_per_price = []
for _ in range(topping_num):
    topping_cal.append(int(input()))

topping_cal.sort(reverse=True)

for i in range(topping_num + 1):
    topping_cal_sum = 0
    if i == 0:
        cal_per_price.append(dough_cal // dough_price)
        continue
    else:
        for j in range(i):
            topping_cal_sum += topping_cal[j]

        cal_per_price.append((dough_cal + topping_cal_sum) // (dough_price + topping_price * (i)))

cal_per_price.sort(reverse=True)
print(cal_per_price[0])

