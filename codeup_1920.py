


def f(n, sub_answer):
    if n > 0:
        sub_answer += str(n % 2)
        f(n//2, sub_answer)
    else:
        answer = ""
        for i in range(len(sub_answer)-1,-1,-1):
            answer += str(sub_answer[i])
        return print(answer)

sub_answer = ""
n = int(input())
f(n, sub_answer)