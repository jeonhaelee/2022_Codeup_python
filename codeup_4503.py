


n = int(input())
m = int(input())

d = [1]
for i in range(m):
    a, b = map(int,input().split())
    if a in d:
        d.append(b)
    elif b in d:
        d.append(a)

d = set(d)
print(len(d))
