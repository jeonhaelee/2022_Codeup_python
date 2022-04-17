

import numpy as np

n = int(input())
stair = np.zeros(n, dtype=np.int64)
for i in range(n):
    stair[n] = int(input())

count = 0
def stairsum():
    for i in range(n):
        if bigger == stair[i]:
            continue
        if count == 2:
            sum += stair[i+1]
        else:
            bigger = max(stair[i], stair[i+1])
            sum += bigger
            count += 1
            
stairsum()