

def solution(answer, n):
    if n > 0:
        answer *= n
        n -= 1
        solution(answer, n)
    else: return print(answer)

answer = 1
n = int(input())
solution(answer, n)