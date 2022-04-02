

def f(a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    print(a-b)
    
a, b = map(int, input().split())
f(a, b)