

def myabs(num):
    if num.find('.') >= 0:
        print(abs(float(num)))
    else : print(abs(int(num)))
    
myabs(input())

