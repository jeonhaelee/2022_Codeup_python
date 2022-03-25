
import numpy as np

n = int(input())

d = np.arange(n*n) # 0 ~ n*n까지 순서대로 채운 1차원 배열 d 만들어주기
d = d + 1 # d 배열 각 원소에 1씩 더해주기
d.shape = (n,n) # d 배열을 n*n 차원 배열로 만들어주기
d = d.transpose() # d 배열을 d 배열의 전치행렬로 바꿔주기

for i in range(n):
    for j in range(n):
        if j % 2 != 0:
            print(d[n-1-i,j], end = " ")
        else : 
            print(d[i,j], end = " ")
    print()
