

n = int(input())
d = list(map(int, input().split()))

m = []
m = sorted(d)

for i in range(n):
    for j in range(n):
        if d[i] == m[j]:
            print(j, end = " ")



    
    
