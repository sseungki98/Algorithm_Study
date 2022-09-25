N,K=map(int,input().split())
row,col=0,N//2
answer="NO"

while row<=col:
    mid=(row+col)//2
    
    cnt=(mid+1)*((N-mid)+1)     #가로로 mid번 짤랐을 때, 조각의 수
    
    if cnt==K:                  # K번 짜를 수 있다면 "YES" 출력 후 반복 종료
        answer="YES"
        break
    
    if cnt<K:                   # 가로로 자른 횟수와, 세로로 자른 횟수의 차이를 줄이면 cnt가 늘어난다.
        row=mid+1
    else:
        col=mid-1
print(answer)
