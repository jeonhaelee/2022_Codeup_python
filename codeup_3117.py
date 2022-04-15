
d = []
n = int(input())
for i in range(n):
    num = int(input())
    if num == 0:
        del d[-1]
    else: d.append(num)
sum = 0
for number in d:
    sum += number
print(sum)