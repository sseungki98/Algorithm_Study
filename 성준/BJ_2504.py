import sys

brackets=sys.stdin.readline()
stack=[]
answer=0
tmp=1

for i in range(len(brackets)):
    if brackets[i]=='(':    #열린 여는 괄호 일 때 stack에 추가 및 값을 *2
        stack.append('(')
        tmp*=2
    elif brackets[i]=='[':  #닫힌 여는 괄호 일 때 stack에 추가 및 값을 *3
        stack.append('[')
        tmp*=3
    elif brackets[i]==']':  #닫힌 닫힌 괄호 일 때
        if stack and stack[-1]=='[':  #stack의 마지막 값이 닫힌 여는 괄호 여서 짝을 이루고
            if brackets[i-1]=='[':    #바로 직전에 닫혔을 때 누적된 값을 풀고 더해준다.
                answer+=tmp
            stack.pop()               #바로 직전에 닫힌 경우가 아니면, 값의 배수는 이미 곱해졌으므로 pop만 해준다.
            tmp//=3                   #값이 더해졌거나, 괄호가 하나 풀렸으므로 값의 배수를 낮춘다.
        else:
            answer=0
            break
    elif brackets[i]==')':
        if stack and stack[-1]=='(':
            if brackets[i-1]=='(':
                answer+=tmp
            stack.pop()
            tmp//=2
        else:
            answer=0
            break
if stack:                             #stack이 남아 있다면 0을 출력한다.
    print(0)
else:                                 #그렇지 않은 경우 정답 출력
    print(answer)
