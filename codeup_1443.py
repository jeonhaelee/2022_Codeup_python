
n = int(input())

d = []
for i in range(n):
    d.append(int(input()))

for i in range(1,n):
    for j in range(i,0,-1):
        if d[j-1] > d[j]:
            temp = d[j-1]
            d[j-1] = d[j]
            d[j] = temp
        
for i in d:
    print(i)