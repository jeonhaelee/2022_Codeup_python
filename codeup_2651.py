
import math

n, k = map(int,input().split())

def f(n, k):
    answer = 1
    if k == 1:
        answer = n
        return answer
    elif n == k:
        return answer
    else:
        for i in range(k):
            answer *= (n - i)
        return answer/math.factorial(k)
answer = f(n, k)

print(int(answer))