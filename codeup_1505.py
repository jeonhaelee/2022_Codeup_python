

import numpy as np

n = int(input())
d = np.zeros(n*n, dtype=np.int64).reshape(n,n)

row = 0; col = 0
count = 1
while 0 in d:
    for j in range(n):
        d[row, j] = count
        count += 1
        print(d)
    row += 1
    col = j
    for i in range(row, n):
        d[i, col] = count
        count += 1
        print(d)
    row = i
    col -= 1
    for j in range(col-1,-1,-1):
        d[row, j] = count
        count += 1
        print(d)
    row -= 1
    col = j
    for i in range(row-1,-1,-1):
        d[i, col] = count
        count += 1
        print(d)
    row = i
    col += 1
    
print(d)