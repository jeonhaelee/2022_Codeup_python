

d = []
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    d.append((a, b))
d.sort()
for i in range(n):
    print(d[i][0], end = " ")
    print(d[i][1], end = " ")
    print()