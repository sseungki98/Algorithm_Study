# 2022-07-25 (월)

n = int(input()) # n : 관찰 횟수
cnt = 0 # 소가 길을 건너간 최소 횟수
cow_info = [-1] * 10 # 소의 번호는 최대 10 이므로, 10으로 초기화
for _ in range(n):
    # cow_num : 소의 번호, cow_loc : 소의 위치
    cow_num, cow_loc = map(int, input().split())

    if cow_info[cow_num - 1] == -1: # cow_num의 소가 기록되지 않은 상태라면, 위치를 기록
        cow_info[cow_num - 1] = cow_loc
    
    elif cow_info[cow_num - 1] != cow_loc: # cow_num의 소가 기록된 상태이고, 위치가 다른 경우 값은 바꾸고 횟수를 추가
        cow_info[cow_num - 1] = cow_loc
        cnt += 1

print(cnt) # 소가 길을 건너간 최소 횟수를 출력