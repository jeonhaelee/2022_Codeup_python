
n = int(input())

d = []
for i in range(n):
    d.append(int(input()))

answer = []
for i in range(len(d)):
    for j in range(len(d)-1):
        if d[j] > d[j+1]:
            temp = d[j]
            d[j] = d[j+1]
            d[j+1] = temp

for i in d:
    print(i)
    
    