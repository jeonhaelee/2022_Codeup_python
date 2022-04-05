
def myswap(a, b):
    if a > b:
        temp = b
        b = a
        a = temp
    print("{} {}".format(a, b))

a, b = map(int, input().split())
myswap(a, b)