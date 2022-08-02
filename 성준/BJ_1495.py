N,S,M=map(int,input().split())
vol=list(map(int,input().split()))
dp=[]

#초기값 설정
if S+vol[0] <= M:
    dp.append(S+vol[0])
if S-vol[0] >=0:
    dp.append(S-vol[0])
        
for i in range(1,N):
    if not dp:  #가능한 값이 없다면 반복문 종료
        break
    tmp=[]
    while dp: #뒤에 사용 가능한 값들을 이 전 누적값들과 합쳐서 탐색
        val=dp.pop()
        if val+vol[i] <=M:
            tmp.append(val+vol[i])
        if val-vol[i] >=0:
            tmp.append(val-vol[i])
    dp=list(set(tmp)) #중복을 제거하여 다음 반복에 사용될 값들을 삽입
if not dp:  #최종일에 사용가능한 경우의 수가 없다면 -1 출력
    print(-1)
else: #그렇지 않을경우 마지막날에 사용가능한 경우의 수중 최댓값 출력
    print(max(dp))
