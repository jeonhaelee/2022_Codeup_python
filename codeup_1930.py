
import numpy as np

memo = np.zeros(15*15, dtype=np.int64).reshape(15,15)

def supersum(k, n):
    if k == 0:
        return n
    elif memo[k, n] > 0:
        return memo[k, n]
    else:
        for i in range(1, n+1):
            memo[k, n] += supersum(k-1, i)
        return memo[k, n]
    
while True:
    try:
        k, n = map(int, input().split())
        print(supersum(k, n))
    except:
        break
    