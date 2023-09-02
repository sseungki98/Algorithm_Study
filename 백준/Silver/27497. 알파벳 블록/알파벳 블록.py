import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s = deque() #문자열을 저장하는 덱
front = [] #블록이 앞에 추가되었는지, 뒤에 추가되었는지를 저장하는 스택
for _ in range(n):
    tmp = input().strip()
    if tmp[0] == '3': #마지막 블록 삭제
        if s: #문자열이 비어있지 않다면
            if front.pop(): #마지막으로 추가된 블록이 앞이라면
                s.popleft()
            else: #뒤라면
                s.pop()
        else: #비어있다면
            continue
    elif tmp[0] == '1': #뒤에 추가
        s.append(tmp[2])
        front.append(False)
    else: #앞에 추가
        s.appendleft(tmp[2])
        front.append(True)
s = list(s)
if s: #문자열이 비어있지 않다면
    print(''.join(s))
else: #비어있다면
    print(0)