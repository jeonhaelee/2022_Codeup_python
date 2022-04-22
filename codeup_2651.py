

def f(a, b):
    answer = 1
    if b == 1:
        answer = a
        return answer
    elif a == b:
        return answer
    else:
        for i in range(b):
            answer *= (a - i)
        return answer

a, b = map(int,input().split())
answer = f(a, b)

print(int(answer))