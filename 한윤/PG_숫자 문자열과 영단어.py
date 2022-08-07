# 2022-08-07 (일)

def solution(s):
    answer = ""
    
    # 영단어와 숫자에 대한 딕셔너리 값 생성
    dictNumber = {
        "zero" : '0',
        "one" : '1',
        "two" : '2',
        "three" : '3',
        "four" : '4',
        "five" : '5',
        "six" : '6',
        "seven" : '7',
        "eight" : '8',
        "nine" : '9'
    }
    
    engWords = ''
    
    for i in range(len(s)):
        if s[i] < '0' or s[i] > '9': # s[i]가 영단어인 경우
            engWords += s[i] # 해당 단어를 engWords 변수에 더함
        else: # s[i]가 숫자인 경우
            if engWords: # engWords가 빈 문자열이 아닌 경우 (문자열을 저장하던 중, 숫자를 만난 경우)
                answer += dictNumber[engWords] + s[i] # answer에 해당 단어로 이루어진 문자와 현재 숫자인 문자를 추가
                engWords = '' # 문자열 변수를 초기화
            else: # engWords가 빈 문자열인 경우 (연속된 숫자인 경우)
                answer += str(s[i]) # answer에 해당 숫자로 이루어진 문자를 추가
        
        if engWords in dictNumber: # 현재까지 완성된 문자열이 dictNumber 상에 존재하는 경우
            answer += dictNumber[engWords]
            engWords = ''
    
    answer = int(answer) # 문자열을 int형으로 형변환
    
    return answer
