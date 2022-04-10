
n = input()

num = ""
sum = 0
for i in range(len(n)-1,-1,-1):
    num += n[i]
    sum += int(n[i])
    
num = int(num)
print(num)
print(sum)
