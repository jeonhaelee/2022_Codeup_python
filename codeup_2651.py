

def f(a, b):
    answer = 1
    for i in range(b):
        answer *= (a - i)
    return answer
    
import math
a, b = map(int,input().split())
answer = f(a, b)

print(int(answer/2))