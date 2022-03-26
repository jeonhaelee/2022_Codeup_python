import numpy as np

n, m = map(int,input().split())

d = np.arange(n*m).reshape(n,m)

num = 1
if m % 2 == 0:
    for j in range(m):
        if j % 2 == 0:
            for i in range(n):
                d[n-1-i,m-1-j] = num
                num += 1
        else :
            for i in range(n):
                d[i,m-1-j] = num
                num += 1
else :
    for j in range(m):
        if j % 2 != 0:
            for i in range(n):
                d[i,m-1-j] = num
                num += 1
        else :
            for i in range(n):
                d[n-1-i,m-1-j] = num
                num += 1
        
for i in range(n):
    for j in range(m):
        print(d[i,j], end = " ")
    print()