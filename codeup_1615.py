
def df(n): # n의 각 자릿수 숫자들과 n 자신을 더한 숫자를 리턴하는 함수 정의
    sum = n
    word = str(n)
    for i in range(len(word)):
        sum += int(word[i])
    return sum

def sum_self_number(a, b):  # a, b 사이의 숫자들 중 셀프 넘버들의 합을 구하는 함수 정의
    d = []
    
    num = 1
    while num <= b:         # num을 1부터 b 까지 반복하며, df(num)를 구해 리스트 d에 넣어주기
        d.append(df(num))
        num += 1
        
    sum = 0
    for i in range(a, b+1): # a, b 사이의 숫자들 중 d에 속하지 않는(=제네레이트가 없는) 셀프 넘버라면,
        if i in d:          # sum에 더해주는 for문
            continue
        else : sum += i
    print(sum)

a, b = map(int, input().split())
sum_self_number(a, b)
