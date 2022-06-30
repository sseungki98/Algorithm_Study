# 2022-06-28 (화)

def d(n): # n과 n의 각 자리 수를 더하는 함수
    data = str(n) # int 형 n을 str 형으로 형 변환
    n_sum = n # 각 자리 수의 합을 저장 하는 변수

    for x in data:
        n_sum += eval(x)

    return n_sum

constructor = [] # 생성자가 있는 숫자를 담는 리스트
for i in range(1, 10001): # 생성자가 있는 숫자를 리스트에 추가
    constructor.append(d(i))

for i in range(1, 10001): # 리스트에 없는 원소만 출력
    if constructor.count(i) == 0:
        print(i)