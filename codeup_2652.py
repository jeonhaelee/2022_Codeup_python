
import math
import numpy as np

n, k = map(int,input().split())
seats = np.zeros(n, dtype=np.int64)
print(seats)

def f(n, k):
    sum = 1
    count = 0
    for i in range(n):
        if seats[i] == 0:
            count += 1 
    sum *= count
    if k == 1:
        return sum
    else : f(n-3, k-1)

result = 1
if k == 1:
    result = n
else : 
    result = f(n,k)
    result = int(result/2)

print(result)