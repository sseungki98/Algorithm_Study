import sys
import heapq

N = int(input())
board = []
for _ in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    for item in temp:
        if len(board) < N:
            heapq.heappush(board, item)
        else:
            if board[0] < item:
                heapq.heappop(board)
                heapq.heappush(board, item)

print(board[0])
