# 2022-07-04 (월)

n = int(input())
arr = list(map(int, input().split())) # 배열 A에 있는 n개의 수 입력
brr = list(map(int, input().split())) # 배열 B에 있는 n개의 수 입력

'''
# B를 재배열하여 푼 경우

arr.sort() # 배열 A의 오름차순 정렬
brr.sort(reverse=True) # 배열 B의 내림차순 정렬

s = 0 # 문제에서 정의된 함수 값

for i in range(n):
    s += arr[i] * brr[i]

print(s)
'''

# B를 재배열하여 풀지 않은 경우

arr.sort(reverse=True) # 배열 A의 내림차순 정렬
b_rank = [0 for _ in range(len(brr))] # 배열 B에 있는 값의 순위를 인덱스로 나타낸 리스트 (오름차순)
b_index = 0 # 배열 B의 값의 순위를 매기는 인덱스

for i in range(min(brr), max(brr) + 1):
    for j in range(len(brr)):
        if brr[j] == i: # 중복된 값에 대해서는 앞에 있는 값이 인덱스가 더 작음
            b_rank[j] = b_index
            b_index += 1

s = 0 # 문제에서 정의된 함수 값

for i in range(n):
    s += arr[b_rank[i]] * brr[i]

print(s)