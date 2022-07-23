left={1:[0,0],4:[1,0],7:[2,0],'*':[3,0]}
right={3:[0,2],6:[1,2],9:[2,2],'#':[3,2]}
midium={2:[0,1],5:[1,1],8:[2,1],0:[3,1]}

def solution(numbers, hand):
    answer = ''
    leftIdx=[3,0]
    rightIdx=[3,2]
    for number in numbers:
        if number in left:  #왼손 범주 안에 있을 때
            answer+='L'
            leftIdx=left[number]
        elif number in right: #오른손 범주 안에 있을 때
            answer+='R'
            rightIdx=right[number]
        else:
            nowIdx=midium[number] #현재 눌러야 할 키패드의 위치
            if abs(nowIdx[0]-leftIdx[0])+abs(nowIdx[1]-leftIdx[1]) > abs(nowIdx[0]-rightIdx[0])+abs(nowIdx[1]-rightIdx[1]): #오른손이 더 가까울 때
                answer+='R'
                rightIdx=nowIdx
            elif abs(nowIdx[0]-leftIdx[0])+abs(nowIdx[1]-leftIdx[1]) < abs(nowIdx[0]-rightIdx[0])+abs(nowIdx[1]-rightIdx[1]): #왼손이 더 가까울 때
                answer+='L'
                leftIdx=nowIdx
            else: #거리가 같을 때
                if hand=='right': #오른손 잡이라면 오른손으로 입력
                    answer+='R'
                    rightIdx=nowIdx
                else: #왼손잡이라면 왼손으로 입력
                    answer+='L'
                    leftIdx=nowIdx
    return answer
