
word = input()
    
for i in word:
    num1 = ord(i) + 2
    print(chr(num1), end = "")
    
print()

for i in word:
    num2 = ord(i) * 7 % 80 + 48
    print(chr(num2), end = "")