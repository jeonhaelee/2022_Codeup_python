
n, m  = map(int, input().split())

print('+', end="")
for i in range(1, n-1):
    print('-', end="")
print('+')

space = " "
mid = space*(n-2)
for i in range(m-2):
    print('|', end="")
    print(mid, end="")
    print('|')
    
print('+', end="")
for i in range(1, n-1):
    print('-', end="")
print('+')