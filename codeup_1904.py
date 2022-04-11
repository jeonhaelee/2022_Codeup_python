

def print_solution(a, b):
    if a <= b:
        if a % 2 != 0:
            print(a, end=" ")
        a += 1
        print_solution(a, b)

a, b = map(int,input().split())
print_solution(a, b)