

def print_solution(num, n):
    if num <= n:
        print(num)
        num += 1
        print_solution(num, n)

num = 1
n = int(input())
print_solution(num, n)