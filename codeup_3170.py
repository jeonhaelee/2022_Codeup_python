
def get_sum (quiz, dics):
    sum = 0
    for i in range(len(words)):
        if dics[i][0] == quiz:
            sum += dics[i][1]
    return sum

n, m = map(int, input().split())
words = []
dics = []

for i in range(n):
    word, number = input().split()
    words.append(word)
    dics.append((word,int(number)))
    
for i in range(m):
    quiz = input()
    if quiz not in words:
        print(0)
    else:
        if words.count(quiz) >= 2:
            print(get_sum(quiz, dics))
        else:
            print(dics[words.index(quiz)][1])