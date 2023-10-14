N = int(input())
break_btn = int(input())
btn_list = []
if break_btn != 0:
    btn_list = list(map(int, input().split()))
min_move = abs(100 - N)

for num in range(1000001):
    for item in str(num):
        if int(item) in btn_list:
            break
    else:
        min_move = min(min_move, len(str(num)) + abs(num - N))

print(min_move)
