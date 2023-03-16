K, S, N = input().split()
k = [ord(K[0])-64, int(K[1])]
s = [ord(S[0])-64, int(S[1])]
move = {'R':[1, 0], 'L':[-1,0], 'B':[0,-1], 'T':[0,1], 'RT':[1,1], 'LT':[-1,1], 'RB':[1,-1], 'LB':[-1,-1]}

for _ in range(int(N)):
    direction = input()
    kx = k[0] + move[direction][0]
    ky = k[1] + move[direction][1]
    if 0 < kx <= 8 and 0 < ky <= 8:
        if s[0] == kx and s[1] == ky:
            sx = s[0] + move[direction][0]
            sy = s[1] + move[direction][1]
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [kx, ky]
                s = [sx, sy]
        else:
            k = [kx, ky]

kx = k[0] + 64
ky = k[1]
sx = s[0] + 64
sy = s[1]
print(chr(kx)+str(ky))
print(chr(sx)+str(sy))
# R -> x좌표 +1
# L -> x좌표 -1
# B -> y좌표 -1
# T -> y좌표 +1
# RT -> x좌표 +1, y좌표 +1
# LT -> x좌표 -1, y좌표 +1
# RB -> x좌표 +1, y좌표 -1
# LB -> x좌표 -1, y좌표 -1

