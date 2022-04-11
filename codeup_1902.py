

def print_solution(num):
    if num > 0:
        print(num)
        num -= 1
        print_solution(num)

num = int(input())
print_solution(num)