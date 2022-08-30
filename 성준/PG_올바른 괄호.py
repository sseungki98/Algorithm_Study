def solution(s):
    stack=[]
    
    for st in s:
        if st=='(':           #여는 괄호가 나오면 stack에 추가
            stack.append('(')
        else:                 
            if not stack:     #닫는 괄호가 나올 때 여는 괄호가 앞에 존재하지 않으면 올바르지 않으므로 False
                return False
            stack.pop()       #그렇지 않은 경우 닫는 괄호의 짝을 제거
    if stack:                 #여는 괄호가 제대로 닫히지 않았다면 False
        return False
    return True
