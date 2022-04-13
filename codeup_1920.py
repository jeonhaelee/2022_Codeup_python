


def f(n, sub_answer):
    if n > 0:
        sub_answer += str(n % 2)
        f(n//2, sub_answer)
    else:
        return print(sub_answer[::-1])

sub_answer = ""
n = int(input())

if n == 0:
    print(0)
else : f(n, sub_answer)
