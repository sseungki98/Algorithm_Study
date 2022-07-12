n= int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
a=A.copy()
b=B.copy()

for i in range(n):
  max_idx = b.index(max(b))
  A[max_idx] = a[i]
  b[max_idx]=-1
s=0
for i in range(n):
  s+=A[i]*B[i]
print(s)
