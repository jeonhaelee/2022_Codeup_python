

import numpy as np

def upper_bound(n, ki, k):
    for i in range(n):
        if ki[i] > k:
            return print(i+1)
    return print(n+1)

n = int(input())
arr = np.array(input().split(),int)
num = int(input())

upper_bound(n, arr, num)