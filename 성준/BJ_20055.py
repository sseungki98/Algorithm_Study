from collections import deque

N,K=map(int,input().split())
belt=deque(list(map(int,input().split())))
answer=0
robot=deque([])

while belt.count(0)<K:
    #1번 과정    
    belt.rotate(1)                #belt를 한칸 회전
    for i in range(len(robot)):   #로봇 한칸씩 이동
        robot[i]+=1
    if robot and robot[0]==N-1: robot.popleft()

    #2번 과정
    for i in range(len(robot)):
        if robot[i]+1<N and belt[robot[i]+1]>0 and robot[i]+1!=robot[i-1]: #이동 가능하다면 로봇 이동
            robot[i]+=1
            belt[robot[i]]-=1
    if robot and robot[0]==N-1:
        robot.popleft()
        
    #3번 과정        
    if belt[0]:
        robot.append(0) #로봇을 올린다
        belt[0]-=1      #올린칸의 내구도를 감소 시킨다.
    answer+=1
print(answer)
