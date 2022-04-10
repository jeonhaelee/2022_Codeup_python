

import numpy as np

d = np.array(input().split(), dtype=np.int64)
d.sort()

even = 0
for i in range(len(d)-1,-1,-1):
    if d[i] % 2 == 0:
        even = d[i]
        break
        
odd = 0
for i in range(len(d)-1,-1,-1):
    if d[i] % 2 != 0:
        odd = d[i]
        break
    
print(even + odd)