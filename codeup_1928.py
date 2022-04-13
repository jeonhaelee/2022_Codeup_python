

def f(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        n = n/2
        print(int(n))
        f(n)
    else: 
        n = (3*n)+1
        print(int(n))
        f(n)

n = int(input())
print(n)
f(n)