import operator

n = int(input())
d = []
for i in range(n):
    d.append(input().split())
    d[i][1] = int(d[i][1])
d.sort(key = lambda x:-x[1])

print(d[2][0])