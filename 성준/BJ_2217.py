N=int(input())
rope=[int(input()) for _ in range(N)]

answer=0
rope.sort(reverse=True)

while rope:
    answer=max(answer,rope[-1]*N) #가장 작은값이 버틸 수 있는 무게 * 로프의 갯수를 비교
    rope.pop()  #가장 작은 값을 사용하지 않고 그 다음 큰 값부터 사용
    N-=1

print(answer)
