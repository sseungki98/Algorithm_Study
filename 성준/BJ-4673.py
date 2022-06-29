constructor=[0]*10001

for i in range(10001):
    tmp=i
    for num in str(i):  #문자열로 변환하여 각 자릿수를 더하여준다.
        tmp+=int(num)
    if tmp < 10001: #생성자가 있다면 해당 값에 +1을 하여준다.
        constructor[tmp]+=1

for i in range(10001):
    if not constructor[i]:  #생성자가 없는 셀프넘버를 출력한다.
        print(i)
