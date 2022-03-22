sentence = input()

count = 0
for i in range(len(sentence)-3):
    if sentence[i] + sentence[i+1] + sentence[i+2] + sentence[i+3] == 'love':
        count += 1
        
print(count)