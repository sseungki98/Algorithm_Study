# 2022-07-11 (월)
# 해당 문제 풀이는 계수 정렬로 풀이함
# 정석 풀이는 이진 탐색을 활용한 문제 풀이

import sys

n = int(input()) # n : 상근이가 가지고 있는 숫자 카드의 개수
card = list(map(int, sys.stdin.readline().split())) # n개의 숫자 카드에 적혀있는 정수
card_sort = [0] * 20000000 # 숫자 카드의 계수 정렬

for i in range(n):
    card_sort[card[i] + 10000000] += 1 # 숫자 카드에 적혀있는 정수에 10,000,000을 더한 인덱스에 1을 추가

m = int(input()) # m : 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 정수의 개수
data = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    if card_sort[data[i] + 10000000]: # 해당 인덱스에 값이 존재하는 경우 1을 출력
        print(1, end = ' ')
    else: # 해당 인덱스에 값이 존재하지 않는 경우 0을 출력
        print(0, end = ' ')