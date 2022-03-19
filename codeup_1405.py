n = int(input())

d = []
d.append(input().split())

for i in range(n):
    print(d[i], end = " ")

for j in range(n):
    for i in range(n):
        print(d[i], end = " ")
    for i in range(n-1):
        temp = d[i]
        d[i] = d[i+1]
        d[i+1] = temp
    
