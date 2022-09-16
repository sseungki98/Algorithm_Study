# 2022-09-16 (금)

# 배낭 문제 풀이

# n : 물품의 수, k : 준서가 버틸 수 있는 무게
n, k = map(int, input().split())

w = [] # w : 물건의 무게
v = [] # v : 해당 물건의 가치

for _ in range(n):
    tempW, tempV = map(int, input().split())
    w.append(tempW)
    v.append(tempV)

dp = [[0] * (k + 1) for _ in range(n + 1)] # 2차원 dp 테이블 생성 (행 : 물건의 수, 열 : 무게)

for i in range(1, n + 1): # i : i번째 물건
    for j in range(1, k + 1): # j : 현재 배낭의 크기 (1 ~ k)
        if w[i - 1] > j: # 물건의 무게가 배낭의 크기보다 큰 경우
            dp[i][j] = dp[i - 1][j] # 이전의 값을 삽입
        else: # 물건의 무게가 배낭의 크기보다 작거나 같은 경우
            # (1) 이전의 값과 (2) 현재 무게 + 현재 무게를 뺀 이전의 값을 더한 무게 중 최댓값을 삽입
            dp[i][j] = max(dp[i - 1][j], v[i - 1] + dp[i - 1][j - w[i - 1]])

print(dp[n][k]) # 배낭에 넣을 수 있는 물건들의 가치 합의 최댓값 출력