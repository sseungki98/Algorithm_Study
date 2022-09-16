# 2022-09-16 (금)

# 브루트 포스 문제풀이 (배낭 문제풀이도 가능)

from itertools import combinations

n = int(input()) # n : 사람의 수
health = list(map(int, input().split())) # health : 세준이가 인사할 때 잃는 체력
delight = list(map(int, input().split())) # delight : 세준이가 인사할 때 얻는 기쁨

greet = [] # greet : health와 delight 리스트를 한 묶음으로 만든 리스트

for i in range(n):
    greet.append([health[i], delight[i]])

maxValue = 0 # 인사할 때 얻는 기쁨의 최댓값 (정답)

for i in range(1, n + 1): # 1 ~ n 까지 조합의 합 중 최댓값 구하기
    tempList = combinations(greet, i) # 크기가 i인 조합을 리스트로 반환
    for li in tempList:
        healthSize = 0 # 세준이가 인사할 때 잃는 체력의 합
        delightSize = 0 # 세준이가 인사할 때 얻는 기쁨의 합
        for j in range(len(li)):
            healthSize += li[j][0]
        
        if healthSize >= 100: # 체력을 100이상 잃는 경우, 아래 코드 패스
            continue

        for j in range(len(li)):
            delightSize += li[j][1]
        
        if maxValue < delightSize: # 현재 저장되어 있는 최댓값의 크기보다 delightSize의 값이 큰 경우 그 값을 갱신
            maxValue = delightSize

print(maxValue)