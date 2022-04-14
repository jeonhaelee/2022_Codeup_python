
n = int(input())
number = input()
num = number[::-1]
answer = ""
for i in range(n):
    answer += num[i]
    if (i+1) % 3 == 0:
        answer += ','
print(answer[::-1])