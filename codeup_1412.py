word = []
for i in range(97,122+1):
    word.append(chr(i))
    
count = []
for i in range(97,122+1):
    count.append(0)

sentence = input()

for i in range(len(sentence)):
    if sentence[i] in word:
        count[ord(sentence[i])-97] += 1

for i in range(len(count)):
    print("{}:{}".format(word[i], count[i]))
