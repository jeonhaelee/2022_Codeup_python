
import numpy as np

n = int(input())
d = np.arange(n*n).reshape(n,n)
for i in range(n):
    for j in range(n):
        print(d[i,j]+1, end = " ")
    print()