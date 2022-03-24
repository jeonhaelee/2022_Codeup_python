import numpy as np

n, m = map(int,input().split())

arr = np.arange(n*m)
arr.shape = (n,m)
arr.tolist()

for i in range(n-1,-1,-1):
    for j in range(m):
        print(arr[i][j] + 1, end = " ")
    print()