def solution(name):
    joy = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = 0
    move = len(name)-1  #기본 이동 횟수

    for n in name:  #상하 조작 횟수
        tmp = min(joy.index(n)-joy.index('A'),joy.index('Z')-joy.index(n)+1)
        answer+=tmp

    for i in range(len(name)):  #좌우 조작 횟수
        idx=i+1
        while idx<len(name) and name[idx]=='A': #앞의 index부터 연속된 A들을 비교해가며
            idx+=1                              #최소 움직임 방향 개선
        move=min(move,i*2+len(name)-idx,i+2*(len(name)-idx))
    return answer+move
