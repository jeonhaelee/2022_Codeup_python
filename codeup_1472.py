import numpy as np

n, m = map(int,input().split())

d = np.arange(n*m-1,-1,-1) # n*m-1 부터 1씩 감소하는 수 차례대로 n*m개 넣어주기
d = d + 1 # d 배열 각 원소에 1씩 더해주기
d.shape = (n,m) # d 배열을 n*m 차원 배열로 만들어주기

if n % 2 != 0: # n이 홀수일 때
    for i in range(n):
        for j in range(m):
            if i % 2 != 0:
                print(d[i,m-1-j], end = " ")
            else :
                print(d[i][j], end = " ")
        print()
else : # n이 짝수일 때
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                print(d[i,m-1-j], end = " ")
            else :
                print(d[i][j], end = " ")
        print()
