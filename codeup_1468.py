
import numpy as np

n = int(input())

d = np.arange(n*n)
d.shape = (n,n)

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(d[i,j]+1, end = " ")
        else :
            print(d[i,n-1-j]+1, end = " ")
    print()