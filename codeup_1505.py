

import numpy as np

n = int(input())
d = np.zeros(n*n, dtype=np.int64).reshape(n,n)

count = 1
for i in range(n):
    d[0,i] = count
    count += 1
for j in range(1, n):
    d[j,i] = count
    count += 1
for i in range(n-2, -1, -1):
    d[j,i] = count
    count += 1
for j in range(n-2, -1, -1):
    if d[j,i] != 0:
        j += 1
        break
    d[j,i] = count
    count += 1
for i in range(1, n):
    if d[j,i] != 0:
        break
    d[j,i] = count
    count += 1
print(d)

