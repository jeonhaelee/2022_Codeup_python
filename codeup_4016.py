

a, b, c = map(int,input().split())

min_value = min(a,b)
min_value = min(min_value,c)

for i in range(min_value, -1, -1):
    if a % i == 0 and b % i == 0 and c % i == 0:
        print(i)
        break