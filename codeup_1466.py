import numpy as np

n, m = map(int, input().split())
arr = np.arange(n*m)
arr.shape = (n,m)
arr.tolist()

for i in range(n):
    for j in range(m):
        arr[i][j] = (n * m - i) - n * j
        
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()
