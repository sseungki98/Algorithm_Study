N = int(input())
crains = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)

if boxes[0] > crains[0]:
    print(-1)
    exit()

move_count = 0
while boxes:
    for item in crains:
        for box in boxes:
            if item >= box:
                boxes.remove(box)
                break

    move_count += 1

print(move_count)




