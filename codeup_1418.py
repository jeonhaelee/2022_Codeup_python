sentence = input()

for i in range(len(sentence)):
    if sentence[i] == 't':
        print(i+1, end = " ")