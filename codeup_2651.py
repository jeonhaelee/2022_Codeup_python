
import math
a, b = map(int,input().split())
if math.factorial(a)/math.factorial(b) == 1:
    answer = 1
else:
    answer = math.factorial(a)/math.factorial(b)/2
print(int(answer))