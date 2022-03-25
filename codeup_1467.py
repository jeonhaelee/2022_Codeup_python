n, m = map(int, input().split())

for i in range(n-1,-1,-1):
    for j in range(m):
        print((n * m - i) - n * j, end = " ")
    print()