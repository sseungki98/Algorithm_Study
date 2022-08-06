# 2022-08-06 (토)

def numConvert(n, nSize): # 10진수 -> 2진수 변환 함수
    newNum = ""
    while n >= 1:
        if n % 2 == 0:
            newNum = "0" + newNum
            n //= 2
        else:
            newNum = "1" + newNum
            n //= 2
        
        if n == 1:
            newNum = "1" + newNum # 마지막 몫인 1을 문자열에 추가
            break

    if len(newNum) < nSize: # 지도의 크기보다 2진수 길이의 값이 작은 경우, 앞 부분을 0으로 채운다.
        plusZero = nSize - len(newNum)
        for _ in range(plusZero):
            newNum = "0" + newNum
    
    return newNum

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n): # 10진수 -> 2진수 변환
        arr1[i] = numConvert(arr1[i], n)
        arr2[i] = numConvert(arr2[i], n)
    
    for i in range(n):
        temp = ""
        for j in range(n):
            if arr1[i][j] == "1" or arr2[i][j] == "1": # 둘 중 하나라도 벽인 경우, "#" 추가
                temp += "#"
            else: # 둘 다 벽이 아닌 경우, " " 추가
                temp += " "
        answer.append(temp)
    
    return answer