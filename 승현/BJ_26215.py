house = int(input())
snow_per_house = list(map(int, input().split()))

max_snow = 0
answer = 0
for snow in snow_per_house:
    if snow > max_snow:
        max_snow = snow

if sum(snow_per_house) - max_snow >= max_snow:
    answer = max_snow + (sum(snow_per_house) - max_snow*2)//2 + (sum(snow_per_house) - max_snow*2)%2
else:
    answer = max_snow

if answer > 1440:
    print(-1)
else:
    print(answer)