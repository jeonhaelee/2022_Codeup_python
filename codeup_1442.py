
n = int(input())

d = []
for i in range(n):
    d.append(int(input()))

answer = []
for i in range(len(d)):
    min = d[0]
    for j in range(len(d)):
        if d[j] < min:
            min = d[j]
    answer.append(min)
    del d[d.index(min)]

for i in answer:
    print(i)
    
    