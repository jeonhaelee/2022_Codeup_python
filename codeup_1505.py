

import numpy as np

n = int(input())
d = np.zeros(n*n, dtype=np.int64).reshape(n,n)

row = 0; col = 0
count = 1
for j in range(n):
    d[row, j] = count
    count += 1
row += 1
col = j
while 0 in d:
    for i in range(row, n):
        if d[i, col] != 0:
            i -= 1
            break
        d[i, col] = count
        count += 1
    row = i
    col -= 1
    for j in range(col,-1,-1):
        if d[row, j] != 0:
            j += 1
            break
        d[row, j] = count
        count += 1
    row -= 1
    col = j
    for i in range(row,-1,-1):
        if d[i, col] != 0:
            i += 1
            break
        d[i, col] = count
        count += 1
    row = i
    col += 1
    for j in range(col, n):
        if d[row, j] != 0:
            j -= 1
            break
        d[row, j] = count
        count += 1


for i in range(n):
    for j in range(n):
        print(d[i, j], end = " ")
    print()