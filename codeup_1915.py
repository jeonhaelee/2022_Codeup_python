

def plus_plus(a, b, num, count):
    if count == num:
        return print(b)
    if count < num:
        a, b = b, a+b
        count += 1
        plus_plus(a, b, num, count)



num = int(input())
count = 0
a = 1; b = 1
if num == 1 or num == 2:
    print(1)
else:
    num -= 2
    plus_plus(a, b, num, count)

