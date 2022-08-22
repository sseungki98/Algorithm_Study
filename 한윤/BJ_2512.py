# 2022-08-22 (월)

n = int(input()) # n : 지방의 수
# regionPay : 각 지방의 예산요청을 표현하는 n개의 정수
regionPay = list(map(int, input().split()))
regionPay.sort() # 이분 탐색을 위한 오름차순 정렬

m = int(input()) # m : 총 예산을 나타내는 정수

start = 0 # 이분 탐색의 시작 범위
end = max(regionPay) # 이분 탐색의 끝 범위

answer = 0 # 배정된 예산들 중 최댓값을 저장할 변수

while start <= end:
    # 중간 값 설정
    mid = (start + end) // 2
    total = 0 # 지방 예산의 총 합

    for x in regionPay:
        if mid > x:
            total += x
        else:
            total += mid
    
    if total == m:
        answer = mid
        break
    elif total > m:
        end = mid - 1
    else:
        answer = mid # 가장 최댓값을 저장
        start = mid + 1

print(answer)