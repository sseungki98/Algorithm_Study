N=int(input())
cows={ x:-1 for x in range(1,11)} #각 소가 이동한 횟수를 담을 배열

answer=0

for _ in range(N):
    number,location=map(int,input().split()) #소의 번호와 위치가 주어진다.
    if cows[number] < 0:    #이동이 관찰된적이 없다면 기록 생성
        cows[number]=location
    else:
        if cows[number]==location:    #이 전과 같은 위치라면 다음 관찰일지 확인
            continue
        else:    #위치가 달라졌다면 달라진 위치 기록 후 이동횟수 증가
            cows[number]=location
            answer+=1
            
print(answer)
