# 입력이 3 4인 경우 다음과 같이 출력한다.
# 1 3 6 9
# 2 5 8 11
# 4 7 10 12

import numpy as np

n, m = map(int,input().split())

d = np.arange(n*m).reshape(n,m)

num = 1
for j in range(0, n):
    d[j,0] = num + j
    num = num + j

num = 1
for j in range(1,m):
    d[0,j] = d[0,j-1] + 1
    if j > int((m+1)/2):
for j in range(1,m):
    d[n-1,j] = 

for i in range(1,n-1):
    for j in range(1,m):
        d[i,j] = d[i,j-1] + (n-1)
        
print(d)