


import numpy as np

n = int(input())
d = np.arange(n*n).reshape(n,n)
for i in range(n):
    for j in range(n):
        print(d[j,i]+1, end = " ")
    print()