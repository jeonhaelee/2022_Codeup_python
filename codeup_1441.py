n = int(input())
d = []
for i in range(n):
    d.append(int(input()))

for j in range(n):
    for i in range(n-1):
        if d[i] > d[i+1]:
            temp = d[i]
            d[i] = d[i+1]
            d[i+1] = temp
     

for i in d:
    print(i)