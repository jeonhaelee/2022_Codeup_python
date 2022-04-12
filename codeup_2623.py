

a, b = map(int,input().split())

if a > b:
    a, b = b, a

for i in range(a, -1, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break
