N = int(input())
line = list(map(int, input().split()))
store = [0]*N

for i in range(N):
    if i == 0:
        store[i] = line[i]
    else:
        store[i] = max(line[i] + store[i-1], line[i])

print(max(store))

