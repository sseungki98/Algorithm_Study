def solution(survey, choices):
    answer = ''
    category = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(choices)):
        if 4-choices[i]>0: category[survey[i][0]]+=(4-choices[i]) #4보다 낮은 값이면 survey의 앞의 유형에 더 높은 점수
        else: category[survey[i][1]]+=(choices[i]-4)              #4보다 높은 값이면 survey의 뒤의 유혀에 더 높은 점수
    
    #값이 같을 때는 사전순으로 더 높은 값
    if category['R']>=category['T']: answer+='R'  
    else: answer+='T'
    if category['C']>=category['F']: answer+='C' 
    else: answer+='F'
    if category['J']>=category['M']: answer+='J' 
    else: answer+='M'
    if category['A']>=category['N']: answer+='A' 
    else: answer+='N'
    return answer
