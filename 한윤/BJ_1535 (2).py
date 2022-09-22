# 2022-09-22 (목)
# BJ_1535 문제의 Dynamic Programming 버전

n = int(input()) # n : 사람의 수
L = list(map(int, input().split())) # L : 세준이가 인사를 하면 잃는 체력
J = list(map(int, input().split())) # J : 세준이가 인사를 하면 얻는 기쁨

dp = [[0] * (101) for _ in range(n + 1)] # 2차원 dp 테이블 생성

for i in range(1, n + 1):
    for j in range(1, 101):
        if L[i - 1] > j: # 세준이가 얻을 수 있는 기쁨이 j보다 큰 경우
            dp[i][j] = dp[i - 1][j]
        else: # 세준이가 얻을 수 있는 기쁨이 j보다 작은 경우
            dp[i][j] = max(J[i - 1] + dp[i - 1][j - L[i - 1]], dp[i - 1][j])

print(dp[n][99]) # 남은 체력이 1 이상이여야 하므로 99의 체력에서 출력