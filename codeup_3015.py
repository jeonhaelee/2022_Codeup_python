

d = []

n, m = map(int, input().split())

for i in range(n):
    a, b = input().split()
    d.append((a, int(b)))

d.sort(key = lambda x : -x[1])

for i in range(m):
    print(d[i][0])