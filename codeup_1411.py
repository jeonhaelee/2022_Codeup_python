n = int(input())

d = []
for i in range(n):
    d.append(i+1)
    
numbers = []
for i in range(n-1):
    numbers.append(int(input()))
    
for i in range(n):
    if d[i] in numbers:
        continue
    else : print(d[i])