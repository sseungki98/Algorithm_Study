from sys import stdin
input=stdin.readline

N=int(input())
K=int(input())
student=list(map(int,input().split()))
candidate={}

for s in student:
    if s not in candidate.keys(): #새로운 후보가 등록되었다면
        if len(candidate.keys())==N:  #후보자의 액자가 가득 찼다면 투표수가 가장 적은 사람중, 가장 추천받은지 오래된 사람을 제거
            min_val=1000
            min_key=1
            for key,value in candidate.items():
                if value < min_val:
                    min_key=key
                    min_val=value
            candidate.pop(min_key)
        candidate[s]=0
    else:   #기존에 존재하는 후보가 다시 추천되었다면 후보자의 추천 수 증가
        candidate[s]+=1
        
print(" ".join(map(str,sorted(candidate.keys()))))
