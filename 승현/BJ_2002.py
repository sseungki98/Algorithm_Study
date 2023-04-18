import sys

N = int(input())
car_in = []
car_out = []

for _ in range(N):
    car_in.append(sys.stdin.readline().strip())

for _ in range(N):
    car_out.append(sys.stdin.readline().strip())

index = []
count = 0
for i in range(len(car_in)):
    index.append(car_in.index(car_out[i]))

for i in range(len(car_in)):
    for j in range(i+1, len(car_in)):
        if index[i] > index[j]:
            count += 1
            break


print(count)
