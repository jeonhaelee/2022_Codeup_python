
n = int(input())

d = []
for i in range(n):
    d.append(int(input()))

for i in range(1,n):
    for j in range(i):
        if d[i] >= d[j]:
            continue
        else :
            temp = d[i]
            d[i] = d[j-1]
            d[j-1] = temp
            
for i in d:
    print(i)
    