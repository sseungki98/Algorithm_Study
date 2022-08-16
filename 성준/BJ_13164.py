from sys import stdin
input=stdin.readline

N,K=map(int,input().split())
child=list(map(int,input().split()))
diff=[]

for i in range(N-1):  #인접한 학생들간의 차이를 저장
    diff.append(child[i+1]-child[i])

print(sum(sorted(diff,reverse=True)[K-1:])) #차이가 큰 기점을 순서대로 그룹을 나누어 준다
