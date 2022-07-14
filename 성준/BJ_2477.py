N=int(input())
data=[list(map(int,input().split())) for _ in range(6)]

maxWidthIdx=0; maxWidth=0
maxHeightIdx=0; maxHeight=0

for i in range(6):
    if data[i][0]==1 or data[i][0]==2:  #가장 긴 가로변의 위치
        if data[i][1] > maxWidth:
            maxWidth=data[i][1]
            maxWidthIdx=i
    else:
        if data[i][1] > maxHeight:  #가장 긴 세로변의 위치
            maxHeight=data[i][1]
            maxHeightIdx=i

bigArea=maxHeight*maxWidth
#가장 작은 세로,가로 변의 길이는 가장 큰 세로,가로 길이의 바로 옆에 붙어있는 변의 차이임을 이용
smallArea=abs(data[(maxHeightIdx-1)%6][1]-data[(maxHeightIdx+1)%6][1])*abs(data[(maxWidthIdx-1)%6][1]-data[(maxWidthIdx+1)%6][1])

print((bigArea-smallArea)*N)
