dx=[-1,0,1,0]
dy=[0,1,0,-1]

def solution(places):
    answer = []
    for place in places:
        tmp_answer=1
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P':    #P를 만났을 때만 검사
                    for k in range(4):
                        nx=i+dx[k]
                        ny=j+dy[k]
                        if 0<=nx<5 and 0<=ny<5 and place[nx][ny] !='X': 
                            if place[nx][ny]=='P':  #P옆에 P가 존재한다면 거리두기 위반
                                tmp_answer=0
                            elif place[nx][ny]=='O':    #빈 테이블을 두고 옆에 P가 존재한다면 거리두기 위반
                                for idx in range(4):
                                    if idx==(k-2)%4:    #이 때 출발점은 제외
                                        continue
                                    x=nx+dx[idx]
                                    y=ny+dy[idx]
                                    if 0<=x<5 and 0<=y<5 and place[x][y]=='P':
                                        tmp_answer=0    #O를 두고 상하좌우는 모두 맨허튼 거리 2이하
        answer.append(tmp_answer)   #answer의 배열에 tmp_answer 입력    
    return answer
