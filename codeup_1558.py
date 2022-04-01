

def f(n):
    answer = ''
    for i in range(len(n)-1, -1, -1):
        answer += n[i]
    print(int(answer))
    
    

f(input())