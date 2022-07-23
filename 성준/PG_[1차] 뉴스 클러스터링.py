import copy

def solution(str1, str2):
    
    def inter(s1,s2): #교집합을 구하는 함수
        result=[]
        for s in s1:
            if s in s2:
                result.append(s)
                s2.remove(s)
        return result
    
    def union(s1,s2): #합집합을 구하는 함수
        result=[]
        for s in s1:
            if s in s2:
                s2.remove(s)
            result.append(s)        
        return result+s2
    
    s1_list=[]
    s2_list=[]
    
    #연속된 두 문자가 알파벳이라면 대문자로 변환하여 저장
    for i in range(len(str1)-1):
        if (str1[i]+str1[i+1]).isalpha():
            s1_list.append((str1[i]+str1[i+1]).upper()) 
    for i in range(len(str2)-1):
        if (str2[i]+str2[i+1]).isalpha(): 
            s2_list.append((str2[i]+str2[i+1]).upper())
    if not s1_list and not s2_list: #둘 다 공집합이라면 1이기 때문에 65536을 곱한 65536을 리턴
        return 65536
    else:
        inter_list=inter(copy.deepcopy(s1_list),copy.deepcopy(s2_list))
        union_list=union(copy.deepcopy(s1_list),copy.deepcopy(s2_list))
        answer = int((len(inter_list)/len(union_list)*65536)) #자카드 유사도 계산
        return answer
