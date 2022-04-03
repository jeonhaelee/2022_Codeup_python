

def findi(num):
    if num not in d:
        return print(-1)
    for i in range(n):
        if d[i] == num:
            return print(i+1)



n = int(input())
d = list(map(int,input().split()))
num = int(input())
findi(num)