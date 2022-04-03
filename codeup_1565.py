

def lcm(a, b):
    if min(a, b) == b:
        temp = b
        b = a
        a = temp
    for i in range(1, b+1):
        if a * i % b == 0:
            return print(a * i)
            


a, b = map(int, input().split())
lcm(a, b)
    