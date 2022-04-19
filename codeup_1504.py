

import numpy as np

n = int(input())
d = np.arange(n*n).reshape(n,n)

d2 = []
for i in range(n):
    if i % 2 != 0:
        for j in range(n-1,-1,-1):
            d2.append(d[i,j] + 1)
    else:
        for j in range(n):
            d2.append(d[i,j] + 1)
            
d2 = np.array(d2).reshape(n,n)
d2 = d2.T
for i in range(n):
    for j in range(n):
        print(d2[i,j], end = " ")
    print()