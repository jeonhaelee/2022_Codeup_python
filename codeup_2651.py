
import math
a, b = map(int,input().split())

answer = math.factorial(a)/math.factorial(b)/2
print(int(answer))