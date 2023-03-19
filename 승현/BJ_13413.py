N = int(input())

for _ in range(N):
    dots = int(input())
    initial = input()
    objects = input()
    diff_count = 0
    save = {'W': 0, 'B':0}
    total_count = 0
    for i in range(dots):
        if initial[i] is not objects[i]:
            diff_count += 1
            if initial[i] == 'W':
                save['W'] += 1
            elif initial[i] == 'B':
                save['B'] += 1

    if diff_count == 0:
        print(0)
    elif diff_count == 1:
        print(1)
    else:
        B_count = save['B']
        W_count = save['W']
        if B_count > W_count:
            total_count += W_count
            total_count += (B_count - W_count)
        elif B_count < W_count:
            total_count += B_count
            total_count += (W_count - B_count)
        else:
            total_count += B_count

        print(total_count)





