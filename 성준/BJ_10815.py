from sys import stdin

arr=[0]*20000001    #-10,000,000은 index=0, +10,000,000은 index=20,000,000
N=int(stdin.readline())
get_card=list(map(int,stdin.readline().strip().split()))
M=int(stdin.readline())
check_card=list(map(int,stdin.readline().strip().split()))
answer=[]

for card in get_card:
    arr[card+10000000]=1    

for card in check_card: #자기 자신의 index에 바로 접근하여 접근시간 단축
    if arr[card+10000000]:
        answer.append('1')
    else:
        answer.append('0')

print(" ".join(map(str,answer)))    #join 함수를 통한 결과 출력
