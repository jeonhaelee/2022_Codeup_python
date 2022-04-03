

def subsetsum(a, b):
    sum = 0
    for i in range(a-1, b):
        sum += d[i]
    print(sum)
     

n = int(input())
d = list(map(int,input().split()))
a, b = map(int, input().split())
subsetsum(a, b)