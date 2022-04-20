

import numpy as np
from itertools import combinations

n = int(input())
d = np.array(input().split(), dtype=np.int64)

result = np.array(list(combinations(d,2)))
print(result)
answer = np.zeros(len(result)*3, dtype=np.int64).reshape(len(result),3)

for i in range(len(result)):
    answer[i][0] = abs(result[i][0]+result[i][1])
    answer[i][1] = result[i][0]
    answer[i][2] = result[i][1]

print(answer)

min = answer[0][0]
min_idx = 0
for i in range(1, len(answer)):
    if (answer[i][0] < min).all():
        min = answer[i]
        min_idx = i
        
if answer[min_idx][1] > answer[min_idx][2]:
    print(answer[min_idx][2], end=" ")
    print(answer[min_idx][1])
else:
    print(answer[min_idx][1], end=" ")
    print(answer[min_idx][2])