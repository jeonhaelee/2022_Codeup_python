

def gcd(a, b):
    
    if a > b:
        temp = a
        a = b
        b = temp
        
    answer = 1
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            answer = i
            
    print(answer)
    
a, b = map(int, input().split())
gcd(a, b)