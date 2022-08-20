# 2022-08-20 (토)

def binarySearch(arr, target, start, end):
    if start > end:
        return
    # 중간 인덱스 값 설정
    mid = (start + end) // 2
    
    # 배열의 해당 인덱스 값과 target값이 일치하는 경우 리턴
    if arr[mid] == target:
        return mid
    # 배열의 해당 인덱스 값보다 target값이 큰 경우, 시작 값을 재설정 한 뒤 재귀함수 호출
    elif arr[mid] < target:
        return binarySearch(arr, target, mid + 1, end)
    # 배열의 해당 인덱스 값보다 target값이 작은 경우, 끝 값을 재설정 한 뒤 재귀함수 호출
    else:
        return binarySearch(arr, target, start, mid - 1)

n = int(input())
xList = list(map(int, input().split()))

xSortList = set(xList) # xList를 set으로 변경 (중복 제거)
xSortList = list(xSortList) # xSortList를 list로 변경
xSortList.sort() # xSortList를 오름차순으로 정렬

for x in xList:
    print(binarySearch(xSortList, x, 0, len(xSortList) - 1), end=' ')