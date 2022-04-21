

def f(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

n = int(input())

answer = 0
for i in range(1, n+1):
    answer += f(i)
print(answer)