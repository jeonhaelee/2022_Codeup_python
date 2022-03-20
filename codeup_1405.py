n = int(input())

d = input().split()

for i in range(n):
    print(d[i], end = " ")
    
print()

for j in range(n-1):
    for i in range(n-1):
        temp = d[i]
        d[i] = d[i+1]
        d[i+1] = temp
    for i in range(n):
        print(d[i], end = " ")
    print()
    
