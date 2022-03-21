n, limit = map(int,input().split())

d = list(map(int,input().split()))
d.sort()

for i in range(0,len(d)):
    if i != 0:
        if i % limit == 0:
            print()
    print(d[i], end = " ")

