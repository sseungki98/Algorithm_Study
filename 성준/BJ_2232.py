from sys import stdin
input=stdin.readline

N=int(input())
arr=[int(input()) for _ in range(N)]

if N==1:    #N=1일 때, 지뢰 하나를 터뜨리고 종료
    print(1)
else:       
    if arr[0]>=arr[1]:  #첫번째 지뢰가 다음 지뢰보다 크거나 같을 경우 먼저 터뜨린다
        print(1)
    for i in range(1,N-1):  #양쪽을 터뜨릴 수 있는 경우 터뜨린다. 만약, 터지지 않는다면 뒤의 더 큰 값에 의해 연속적으로 터지게 된다.
        if arr[i-1]<=arr[i]>=arr[i+1]:
            print(i+1)
    if arr[N-1]>=arr[N-2]:  #마지막 지뢰가 그 전 지뢰보다 크거나 같아서 터지지 않았다면 터뜨려준다.
        print(N)
