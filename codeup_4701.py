
import numpy as np
n = int(input())
d = np.array(input().split(), dtype=np.int64)

zero = abs(d[0]+d[1])
index_i = 0
index_j = 1
for i in range(n-1):
    for j in range(i+1, n):
        test = abs(d[i]+d[j])
        if test < zero:
            zero = test
            index_i = i
            index_j = j

if d[index_i] > d[index_i]:
    print(d[index_j], end = " ")
    print(d[index_i])
else:
    print(d[index_i], end = " ")
    print(d[index_j])