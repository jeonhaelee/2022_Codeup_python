# N개의 입력 데이터가 주어지면 정렬해서 출력하시오.
# 입력 예)
# 5
# 2 5 8 1 2
# 출력 예)
# 1 2 2 5 8

import numpy as np

n = int(input())
d = np.array(input().split(), dtype=int)

over = int(d[np.argmax(d)]) + 1
for i in range(n):
    min = d[np.argmin(d)]
    print(min, end = " ")
    d[np.argmin(d)] = over







 