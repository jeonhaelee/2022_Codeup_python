
n = int(input())
d = list(map(int,input().split()))

d.sort(reverse=True)

for i in d:
    print(i, end = " ")
    
    