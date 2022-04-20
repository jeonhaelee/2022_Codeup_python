

import numpy as np
from itertools import combinations

n = int(input())
d = np.array(input().split(), dtype=np.int64)
result = list(combinations(d,2))
answer = []
for i in range(len(result)):
    answer.append((abs(result[i][0]+result[i][1]), result[i][0], result[i][1]))
answer.sort(key=lambda x:x[0])
if answer[0][1] > answer[0][2]:
    print(answer[0][2], end=" ")
    print(answer[0][1])
else:
    print(answer[0][1], end=" ")
    print(answer[0][2])

# d = [1, 2, 3]
# result = list(combinations(d,2))
# answer = []
# for i in range(len(result)):
#     answer.append((result[i][0]+result[i][1], result[i][0], result[i][1]))
# answer.sort(key=lambda x:x[0])
# if answer[0][1] > answer[0][2]:
#     print(answer[0][2], end=" ")
#     print(answer[0][1])
# else:
#     print(answer[0][1], end=" ")
#     print(answer[0][2])