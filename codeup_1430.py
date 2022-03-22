n = int(input())
d = list(map(int,input().split()))

m = int(input())
q = list(map(int,input().split()))

for i in range(m):
    if q[i] in d:
        print(1, end = " ")
    else : print(0, end = " ")