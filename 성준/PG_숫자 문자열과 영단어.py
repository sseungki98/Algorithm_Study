import re

def solution(s):
    answer=[]
    dic={ 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    alpha=(re.findall('[a-z]',s))
    if alpha:
        tmp=""
        for a in alpha: #문자열을 전부 숫자로 변경
            tmp+=a
            if tmp in dic:
                s=s.replace(tmp,str(dic[tmp]))
                tmp=""
        return int(s)
    return int(s)
