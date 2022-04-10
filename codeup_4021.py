

import numpy as np

d = np.array(input().split(), dtype=np.int64)
sum = 0
for num in d:
    if num % 2 != 0:
        sum += num
if sum == 0:
    print(-1)
else : print(sum)