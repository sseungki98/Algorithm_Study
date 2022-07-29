from sys import stdin
import copy
from bisect import bisect_left

N=int(stdin.readline())
target=list(map(int,stdin.readline().split()))
q=list(set(copy.deepcopy(target)))  #중복제거 후 list 복사
q.sort()  #q 정렬

for t in target:  #q에서자신의 index를 이진탐색을 통해 탐색
    print(bisect_left(q,t),end=" ")
