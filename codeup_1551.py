

def f(n, d, k):
    for i in range(n):
        if k == d[i]:
            return print(i+1)
    return print(-1)
    


n = int(input())
d = list(map(int,input().split()))
k = int(input())

f(n, d, k)