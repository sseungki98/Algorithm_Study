def find(num,cnt):
    global answer
    if num==B:  #숫자가 B로 변환된 경우
        answer=min(answer,cnt)
        return
    if num > B: #변환된 숫자가 B보다 커지면 return
        return
    find(int(str(num)+'1'),cnt+1) #뒤에 1을 붙히기
    find(num*2,cnt+1) #*2를 해보기

A,B=map(int,input().split())
answer=10**9
find(A,0)
if answer==10**9: #답이 없는 경우
    print(-1)
else:
    print(answer+1) #최소값에 +1 해서 출력
