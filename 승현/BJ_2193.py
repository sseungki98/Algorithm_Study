num = int(input())

if num == 1 or num == 2:
    print(1)
else:
    cur_num, next_num = 1, 1
    for i in range(num-2):
        cur_num, next_num = next_num, cur_num + next_num
    print(next_num)





