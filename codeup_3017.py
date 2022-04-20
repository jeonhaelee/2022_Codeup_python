n = int(input())
d = []
for i in range(n):
    a, b = map(int,input().split())
    d.append((i+1, a, b))
d.sort(key=lambda x:(-x[1],-x[2],x[0]))
for i in range(n):
    print(d[i][0],end=" ")
    print(d[i][1],end=" ")
    print(d[i][2])