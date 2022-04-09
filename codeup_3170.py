
import sys

n, m = map(int, input().split())

dics = {}
for i in range(n):
    word, number = sys.stdin.readline().rstrip().split()
    number = int(number)
    if word in dics.keys():
        dics[word] += number
    else : dics[word] = number
    
for i in range(m):
    quiz = sys.stdin.readline().rstrip()
    print(dics[quiz])



