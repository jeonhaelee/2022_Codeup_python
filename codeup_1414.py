sentence = input()

count_1 = 0; count_2 = 0

for i in range(len(sentence)-1):
    if sentence[i] == 'c' or sentence[i] == 'C':
        count_1 += 1
        if sentence[i+1] == 'c' or sentence[i+1] == 'C':
            count_2 += 1
if sentence[-1] == 'c' or sentence[-1] == 'C':
        count_1 += 1
        
print(count_1)
print(count_2)