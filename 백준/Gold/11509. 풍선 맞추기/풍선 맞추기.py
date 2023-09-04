N = int(input())
ballons = list(map(int, input().split()))

flag = [0] * 1000001

ans = 0
for i in range(len(ballons)):
    if flag[ballons[i]] == 0:
        ans+=1
        flag[ballons[i] - 1] += 1
    else:
        flag[ballons[i]] -= 1
        flag[ballons[i] - 1] += 1
        
print(ans)  