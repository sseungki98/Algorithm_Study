def solution(s):
    answer=sorted(list(map(int,s.split())))   #정렬된 배열을 저장
    return str(answer[0])+' '+str(answer[-1])
