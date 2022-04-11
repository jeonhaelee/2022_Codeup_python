
import sys
sys.setrecursionlimit(20000)

def sum_solution(sum, num, n):
    if num <= n:
        sum += num
        num += 1
        sum_solution(sum, num, n)
    else: return print(sum)

sum = 0; num = 1
n = int(input())
sum_solution(sum, num, n)