from sys import stdin
import copy

N,M,R=map(int,stdin.readline().split())
arr=[list(map(int,stdin.readline().split())) for _ in range(N)]
operation=list(map(int,stdin.readline().split()))

for op in operation:
    if op==1:   #1번 연산
        for k in range(len(arr)//2):
            tmp=arr[k]
            arr[k]=arr[len(arr)-k-1]
            arr[len(arr)-k-1]=tmp
    elif op==2: #2번 연산
        for i in range(len(arr)):
            for k in range(len(arr[0])//2):
                tmp=arr[i][k]
                arr[i][k]=arr[i][len(arr[0])-k-1]
                arr[i][len(arr[0])-k-1]=tmp
    elif op==3: #3번 연산
        arr=list(map(list,zip(*arr[::-1]))) #시계 방향으로 회전
    elif op==4: #4번 연산
        arr=list(map(list,zip(*arr)))[::-1] #반시계 방향으로 회전
    elif op==5: #5번 연산
        tmp=copy.deepcopy(arr[:len(arr)//2])
        for i in range(len(arr)//2):   #4번을 1번으로
            for j in range(len(arr[0])//2):
                arr[i][j]=arr[i+len(arr)//2][j]
        for i in range(len(arr)//2):   #3번을 4번으로
            for j in range(len(arr[0])//2):
                arr[i+len(arr)//2][j]=arr[i+len(arr)//2][j+len(arr[0])//2]
        for i in range(len(arr)//2):   #2번을 3번으로
            for j in range(len(arr[0])//2):
                arr[i+len(arr)//2][j+len(arr[0])//2]=arr[i][j+len(arr[0])//2]
        for i in range(len(arr)//2):   #1번을 2번으로
            for j in range(len(arr[0])//2):
                arr[i][j+len(arr[0])//2]=tmp[i][j]
    elif op==6: #6번 연산
        tmp=copy.deepcopy(arr[len(arr)//2:len(arr)])
        for i in range(len(arr)//2):   #1번을 4번으로
            for j in range(len(arr[0])//2):
                arr[i+len(arr)//2][j]=arr[i][j]
        for i in range(len(arr)//2):   #2번을 1번으로
            for j in range(len(arr[0])//2):
                arr[i][j]=arr[i][j+len(arr[0])//2]
        for i in range(len(arr)//2):   #3번을 2번으로
            for j in range(len(arr[0])//2):
                arr[i][j+len(arr[0])//2]=arr[i+len(arr)//2][j+len(arr[0])//2]
        for i in range(len(arr)//2):   #4번을 3번으로
            for j in range(len(arr[0])//2):
                arr[i+len(arr)//2][j+len(arr[0])//2]=tmp[i][j]
for a in arr:
    print(" ".join(map(str,a)))
