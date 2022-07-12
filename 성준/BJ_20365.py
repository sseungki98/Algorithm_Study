from sys import stdin

N=int(stdin.readline())
blog=list(map(str,stdin.readline().strip()))
stack=[blog[0]]

for i in range(1,len(blog)):    #BBBRRRBBR = BRBR 로 만드는 과정
    if blog[i]==stack[-1]:
        continue
    stack.append(blog[i])
    
bcnt=stack.count('B')    #B의 갯수를 세어준다.
print(min(len(stack)-bcnt,bcnt)+1)  #만약 BRBRB면 B로 전체를 한번 칠해주고 R을 2번 칠해주면 된다.
