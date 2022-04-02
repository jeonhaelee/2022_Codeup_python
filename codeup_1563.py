

def mid(a, b, c):
    d = [a, b, c]
    d.sort()
    print(d[1])
    
a, b, c = map(int, input().split())
mid(a, b, c)