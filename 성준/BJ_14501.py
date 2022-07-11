N=int(input())

def back(date,sum_val,idx): #소요되는 시간,누적 이득,현재 일자를 parameter로 받음
    global answer
    if date+idx > N:  #현재 일자부터 소요되는 시간이 N 초과시 완성이 불가능 하므로 return
        return
    answer=max(sum_val,answer)  #현재 일자부터 소요되는 시간이 N 이하이면 해당 일까지의 누적 이득 비교
    for i in range(date+idx,N): #현재 시작가능한 일자부터, N 까지 다시 탐색
        back(advice_list[i][0],sum_val+advice_list[i][1],advice_list[i][1],i)
    
advice_list=[]
answer=0

for i in range(N):
    date,benefit=map(int,input().split())
    advice_list.append([date,benefit])

for i in range(N):
    back(advice_list[i][0],advice_list[i][1],i)

print(answer)
