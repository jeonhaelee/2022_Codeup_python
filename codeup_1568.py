

def maxi(a, b):
    max = d[a-1]
    for i in range(a, b+1):
        if d[i-1] > max:
            max = d[i-1]
    print(d.index(max)+1)
     

n = int(input())
d = list(map(int,input().split()))
a, b = map(int, input().split())
maxi(a, b)