def solution(n, arr1, arr2):
    answer = []
    for arr in zip(arr1,arr2):
        ar=bin(arr[0]|arr[1])[2:].zfill(n)  #2진수 or bit연산자를 사용하고, 문자열 slice를 통해 0b를 제거 후 자릿수 0을 맞춰준다.
        ar=ar.replace('1','#')  #1을 #으로 변환
        ar=ar.replace('0',' ')  #0을 공백으로 변환
        answer.append(ar)
    return answer
