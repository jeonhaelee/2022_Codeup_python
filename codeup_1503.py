
import numpy as np

n = int(input())
d = np.arange(n*n).reshape(n,n)

for i in range(n):
    if i % 2 != 0:
        for j in range(n-1,-1,-1):
            print(d[i,j] + 1, end = " ")
        print()
    else:
        for j in range(n):
            print(d[i,j] + 1, end = " ")
        print()
