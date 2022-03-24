import numpy as np

n = int(input())

arr = np.arange(1,n*n+1)
arr.shape = (n,n)
arr.tolist()

for i in range(n):
    for j in range(n-1,-1,-1):
        print(arr[i][j], end = " ")
    print()