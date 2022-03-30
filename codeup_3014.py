# N개의 입력 데이터가 주어지면 정렬해서 출력하시오.
# 입력 예)
# 5
# 2 5 8 1 2
# 출력 예)
# 1 2 2 5 8

import numpy as np

n = int(input())
d = np.array(input().split(), dtype=int)

count = np.zeros(100001,dtype=int)
answer = [0] * n

for i in d:
    count[i] += 1
    
for i in range(1,100001):
    count[i] += count[i-1]
   
for i in range(n):
    answer[count[d[i]]-1] = d[i]
    count[d[i]] -= 1

for i in answer:
    print(i, end = " ")




 