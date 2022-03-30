

def zero(n):
    if n == 0:
        print("zero")

def plus(n):
    if n > 0:
        print("plus")
    elif n < 0 :
        print("minus")
    
num = int(input())
zero(num)
plus(num)