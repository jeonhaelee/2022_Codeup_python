

def mysubstr(word, a, b):
    print(word[a:a+b])
    
word = input()
a, b = map(int, input().split())

mysubstr(word, a, b)