

n, m = map(int, input().split())

dics = {}
for i in range(n):
    word, number = input().split()
    number = int(number)
    if word in dics.keys():
        dics[word] += number
    else : dics[word] = number
    
for i in range(m):
    quiz = input()
    if quiz not in dics.keys():
        print(0)
    else : print(dics[quiz])
    



