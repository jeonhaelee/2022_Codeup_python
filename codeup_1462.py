import numpy as np

n = int(input())

arr = np.arange(n*n)
arr.shape = (n,n)
arr.tolist()

for i in range(n):
    for j in range(n):
        arr[i][j] = (i+1) + (n*j)


for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()